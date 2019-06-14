from marshmallow import Schema, fields, pprint, post_load, validates, validates_schema, ValidationError
from datetime import datetime
from logging import info, debug, error
'''
Pre-/Post-processor Invocation Order
In summary, the processing pipeline for deserialization is as follows:

@pre_load(pass_many=True) methods
@pre_load(pass_many=False) methods
load(in_data, many) (validation and deserialization)
@post_load(pass_many=True) methods
@post_load(pass_many=False) methods
The pipeline for serialization is similar, except that the “pass_many” processors are invoked after the “non-raw” processors.

@pre_dump(pass_many=False) methods
@pre_dump(pass_many=True) methods
dump(obj, many) (serialization)
@post_dump(pass_many=False) methods
@post_dump(pass_many=True) methods
'''


class User(object):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.created_at = datetime.utcnow()
        self.friends = []
        self.employer = None

    def __repr__(self):
        return '<User(name={self.name!r})>'.format(self=self)

    '''
    Deserializing to Objects
    In order to deserialize to an object, define a method of your Schema and decorate it with post_load. The method receives a dictionary of deserialized data as its only parameter.
    '''
    @post_load
    def make_user(self, data):
        return User(**data)


class Blog(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author  # a User object
        self.collaborators = None

    def set_collaborators(self, collaborators):
        self.collaborators = collaborators


'''
Handling Errors
By default, Schema.dump() and Schema.load() will raise a ValidationError.

You can specify a custom error-handling function for a Schema by overriding the handle_error method. The method receives the ValidationError and the original object (or input data if deserializing) to be (de)serialized.
'''


class AppError(Exception):
    pass


'''Nesting A Schema Within Itself'''


class UserSchema(Schema):
    name = fields.String(
        required=True,
        error_messages={'required': 'name is required'}
    )
    email = fields.Email(
        required=True,
        error_messages={'required': 'email is required'}
    )

    age = fields.Integer(
        required=True,
        error_messages={'required': 'Age is required'}
    )

    # created_at is "read-only"
    created_at = fields.DateTime(dump_only=True)

    # password is "write-only"
    password = fields.String(load_only=True)

    upper_name = fields.Function(lambda obj: obj.name.upper())

    # missing is used for deserialization if the field is not found in the input data
    uuid = fields.UUID(missing='337d946c-32cd-11e8-b475-0022192ed31b')

    # default is used for serialization if the input value is missing
    birthdate = fields.DateTime(default=datetime(2017, 9, 29))

    friends = fields.Nested('self', many=True)

    # use the 'exclude' argument to avoid infinite recursion
    employer = fields.Nested('self', exclude=('employer', ), default=None)

    class Meta:
        ordered = True

    # field level validation
    @validates('age')
    def validate_age(self, value):
        if value < 0:
            raise ValidationError('Age must be grater than 0')
        if value > 30:
            raise ValidationError('Age must be smaller than 30')

    # schema-level validation
    @validates_schema
    def validate_numbers(self, data):
        if data['name'] == data['email']:
            raise ValidationError('name do not be equal email')

    # Storing Errors on Specific Fields
    @validates_schema
    def validate_lower_bound(self, data):
        errors = {}
        if data['field_b'] <= data['field_a']:
            errors['field_b'] = ['field_b must be greater than field_a']
        if data['field_c'] <= data['field_a']:
            errors['field_c'] = ['field_c must be greater than field_a']
        if errors:
            raise ValidationError(errors)

    # Storing Errors on Specific Fields
    @validates_schema
    def validate_upper_bound(self, data):
        errors = {}
        if data['field_b'] >= data['field_d']:
            errors['field_b'] = ['field_b must be lower than field_d']
        if data['field_c'] >= data['field_d']:
            errors['field_c'] = ['field_c must be lower than field_d']
        if errors:
            raise ValidationError(errors)
    # customized Handling Errors

    def handle_error(self, exc, data):
        """Log and raise our custom exception when (de)serialization fails."""
        error(exc.messages)
        raise AppError(f'An error occurred with input: {data}')


class BlogSchema(Schema):
    title = fields.String()
    author = fields.Nested(UserSchema, only=["email"])
    collaborators = fields.Nested(UserSchema, many=True)


class SiteSchema(Schema):
    blog = fields.Nested(BlogSchema)


'''Two-way Nesting'''


class AuthorSchema(Schema):
    # Make sure to use the 'only' or 'exclude' params
    # to avoid infinite recursion
    books = fields.Nested('BookSchema', many=True, exclude=('author', ))

    class Meta:
        fields = ('id', 'name', 'books')


class BookSchema(Schema):
    author = fields.Nested(AuthorSchema, only=('id', 'name'))

    class Meta:
        fields = ('id', 'title', 'author')


user = User(name="Monty", email="monty@python.org", age=24)
user_schema = UserSchema()
'''
dump(obj, many=None)
Serialize an object to native Python data types according to this Schema’s fields.

Parameters:	
obj – The object to serialize.
many (bool) – Whether to serialize obj as a collection. If None, the value for self.many is used.
Returns:	
A dict of serialized data

Return type:	
dict

New in version 1.0.0.

Changed in version 3.0.0b7: This method returns the serialized data rather than a (data, errors) duple. A ValidationError is raised if obj is invalid.
'''
result = user_schema.dump(user)
print(type(result))
pprint(result)

'''
dumps(obj, many=None, *args, **kwargs)
Same as dump(), except return a JSON-encoded string.

Parameters:	
obj – The object to serialize.
many (bool) – Whether to serialize obj as a collection. If None, the value for self.many is used.
Returns:	
A json string

Return type:	
str

New in version 1.0.0.

Changed in version 3.0.0b7: This method returns the serialized data rather than a (data, errors) duple. A ValidationError is raised if obj is invalid.
'''
# result = user_schema.dumps(user)
# print(type(result))
# pprint(result)


'''Filtering output'''
summary_schema = UserSchema(only=('name', 'email'))
result = summary_schema.dump(user)
pprint(result)


'''Deserializing Objects (“Loading”)'''
user_data = {
    'email': u'ken@yahoo.com',
    'name': u'Ken'
}
schema = UserSchema()
result = schema.load(user_data)
print(type(result))
pprint(result)


'''Deserializing Collections'''
user1 = User(name="Mick", email="mick@stones.com", age=24)
user2 = User(name="Keith", email="keith@stones.com", age=24)
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
pprint(result)


'''
load(data, many=None, partial=None)
Deserialize a data structure to an object defined by this Schema’s fields and make_object().

Parameters:	
data (dict) – The data to deserialize.
many (bool) – Whether to deserialize data as a collection. If None, the value for self.many is used.
partial (bool|tuple) – Whether to ignore missing fields. If None, the value for self.partial is used. If its value is an iterable, only missing fields listed in that iterable will be ignored.
Returns:	
A tuple of the form (data, errors)

Return type:	
UnmarshalResult, a collections.namedtuple
'''
'''Validation'''
data, errors = UserSchema().load({'email': 'foo'})
print(errors)

'''
loads(json_data, many=None, *args, **kwargs)
Same as load(), except it takes a JSON string as input.

Parameters:	
json_data (str) – A JSON string of the data to deserialize.
many (bool) – Whether to deserialize obj as a collection. If None, the value for self.many is used.
partial (bool|tuple) – Whether to ignore missing fields. If None, the value for self.partial is used. If its value is an iterable, only missing fields listed in that iterable will be ignored.
Returns:	
A tuple of the form (data, errors)

Return type:	
UnmarshalResult, a collections.namedtuple
'''
result = UserSchema(many=True).load([{'email': 'foo1'}, {'email': 'foo2'}, {'email': 'foo3'}])
print(result.errors)

'''custom validation'''
result = UserSchema().load({'age': 100})
print(result.errors)

'''Ordering Output'''
schema = UserSchema()
result = schema.dump(user)
# marshmallow's pprint function maintains order
pprint(result, indent=2)


user = User(name="Monty", email="monty@python.org", age=24)
blog = Blog(title="Something Completely Different", author=user)
result = BlogSchema().dump(blog)
pprint(result)


schema = SiteSchema(only=['blog.author.email'])
result = schema.dump({})
pprint(result)


'''Nesting A Schema Within Itself'''
user = User('Steve', 'steve@example.com', 25)
user.friends.append(User('Mike', 'mike@example.com', 24))
user.friends.append(User('Joe', 'joe@example.com', 28))
user.employer = User('Dirk', 'dirk@exampl.com', 30)

result = UserSchema().dump(user)
pprint(result, indent=2)
