from datetime import datetime

from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy

from marshmallow import Schema, fields, ValidationError, pre_load


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(80))
    last = db.Column(db.String(80))


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author_id'))
    author = db.relationship('Author', backref='owner', lazy='dynamic')
    posted_at = db.Column(db.DateTime)


db.create_all()


class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    first = fields.Str()
    last = fields.Str()
    formatted_name = fields.Method('format_name', dump_only=True)

    def format_name(self, author):
        return f'{author.last}, {author.first}'


def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided.')


class QuoteSchema(Schema):
    id = fields.Int(dump_only=True)
    author = fields.Nested(AuthorSchema, validate=must_not_be_blank)
    content = fields.Str(required=True, validate=must_not_be_blank)
    posted_at = fields.DateTime(dump_only=True)

    # Allow client to pass author's full name in request body
    # e.g. {"author': 'Tim Peters"} rather than {"first": "Tim", "last": "Peters"}
    @pre_load
    def process_author(self, data):
        author_name = data.get('author')
        if author_name:
            first_name, last_name = author_name.split(' ')
            author_dict = dict(first=first_name, last=last_name)
        else:
            author_dict = {}
        data['author'] = author_dict
        return data


author_schema = AuthorSchema()
quote_schema = QuoteSchema()

authors_schema = AuthorSchema(many=True)
quotes_schema = quote_schema(many=True, only=('id', 'content'))


##### API #####
@app.route('/authors')
def get_authors():
    authors = Author.query.all()
    # Serialize the query set
    result = authors_schema.dump(authors)
    return jsonify({'authors': result})


@app.route('/authors/<int:id>')
def get_author(id):
    try:
        author = Author.query.get(id)
    except:
        return jsonify({'message': 'Author couldn\'t be found'}), 400
    author_result = author_schema.dump(author)
    quotes_result = quotes_schema.dump(author.quotes.all())
    return jsonify({'author': author_result, 'quotes': quotes_result})


@app.route('/quotes')
def get_quotes():
    quotes = Quote.query.all()
    result = quotes_schema.dump(quotes, many=True)
    return jsonify({'quotes': result})


@app.route('/quotes/<int:id>')
def get_quote(id):
    try:
        quote = Quote.query.get(id)
    except:
        return jsonify({'message': 'Quote could not be found.'}), 400
    result = quote_schema.dump(quote)
    return jsonify({'quote': result})


@app.route('/quotes', methods=['POST'])
def new_qoute():
    json_data = request.get_json()
    if not json_data:
        return jsonify({'message': 'no input data provided'}), 400

    try:
        data = quotes_schema.load(json_data)
    except ValidationError as err:
        return jsonify(err.messages), 422

    first_name, last_name = data['author']['first'], data['author']['last']
    author = Author.query.filter_by(first=first_name, last=last_name).first()

    if author is None:
        # Create a new author
        author = Author(first=first, last=last)
        db.session.add(author)

    # create new quote
    quote = Quote(
        content=data['content'],
        author=author,
        posted_at=datetime.utcnow()
    )
    db.session.add(quote)
    db.session.commit()

    result = quote_schema.dump(Quote.query.get(quote.id))
    return jsonify({
        'message': 'Created new quote.',
        'quote': result,
    })


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
