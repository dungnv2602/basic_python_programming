from marshmallow_jsonapi import Schema, fields
from marshmallow_jsonapi.exceptions import IncorrectTypeError
from marshmallow import validate, ValidationError, pprint


class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Comment:
    def __init__(self, id, body, author):
        self.id = id
        self.body = body
        self.author = author


class Post:
    def __init__(self, id, title, author, comments=None):
        self.id = id
        self.title = title
        self.author = author
        self.comments = [] if comments is None else comments

def dasherize(text):
    return text.replace('_', '-')

'''
You can optionally specify a function to transform attribute names. For example, you may decide to follow JSON API’s recommendation to use “dasherized” names.
'''
class AuthorSchema(Schema):
    id = fields.Str(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(load_only=True, validate=validate.Length(6))
    twitter = fields.Str()

    class Meta:
        type_ = 'authors'
        strict = True
        inflect = dasherize


class UserSchema(Schema):
    id = fields.String(dump_only=True)
    name = fields.String()

    # The DocumentMeta field is used to serialize the meta object within a document’s “top level”.
    document_meta = fields.DocumentMeta()

    # The ResourceMeta field is used to serialize the meta object within a resource object.
    resource_meta = fields.ResourceMeta()

    class Meta:
        type_ = 'users'
        strict = True


class CommentSchema(Schema):
    id = fields.String(dump_only=True)
    body = fields.String()

    author = fields.Relationship(
        self_url='/comments/{comment_id}/relationships/author',
        self_url_kwargs={'comment_id': '<id>'},
        related_url='/comments/{author_id}',
        related_url_kwargs={'author_id': '<author.id>'},
        type_='users',
        # define a schema for rendering included data
        schema='UserSchema'

    )

    class Meta:
        type_ = 'comments'
        strict = True


class PostSchema(Schema):
    id = fields.String(dump_only=True)
    title = fields.String()

    comments = fields.Relationship(
        related_url='/posts/{post_id}/comments',
        related_url_kwargs={'post_id': '<id>'},
        many=True,
        # include resource linkage
        include_resource_linkage=True,
        type_='comments',
        # define a schema included data
        schema='CommentSchema'
    )

    author = fields.Relationship(
        self_url='/posts/{post_id}/relationships/author',
        self_url_kwargs={'post_id': '<id>'},
        related_url='/authors/{author_id}',
        related_url_kwargs={'author_id': '<author.id>'},
        # include resource linkage
        include_resource_linkage=True,
        type_='users'
    )

    class Meta:
        type_ = 'posts'
        strict = True


armin = User(id='101', name='Armin')
laura = User(id='94', name='Laura')
steven = User(id='23', name='Steven')
comments = [Comment(id='5', body='Marshmallow is sweet like sugar!', author=steven),
            Comment(id='12', body='Flask is Fun!', author=armin)]
post = Post(id='1', title='Django is Omakase', author=laura, comments=comments)


""" schema = PostSchema(include_data=('comments', 'comments.author'))
result = schema.dump(post)
print(result.data) """


""" user = {'name': 'Alice', 'document_meta': {'page': {'offset': 10}}, 'resource_meta': {'active': True}}
result = UserSchema().dump(user)
print(result.data) """

# If an invalid “type” is passed in the input data, an IncorrectTypeError is raised.
author_data = {
    'data': {
        'type': 'authors',
        'attributes': {
            'first_name': 'Dan',
            'password': 'short'
        }
    }
}

try:
    AuthorSchema().validate(author_data)
except IncorrectTypeError as err:
    pprint(err.messages)
