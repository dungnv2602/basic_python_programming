from flask import Flask, request, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from uuid import uuid4
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = 'my-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jwt_demo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    admin = db.Column(db.Boolean)

    todos = db.relationship('Todo', backref='user', lazy=True)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    completed = db.Column(db.Boolean)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


def token_required(func):  # create decorator
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithm='HS256')
            current_user = User.query.filter_by(uuid=data['uuid']).first()
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return func(current_user, *args, **kwargs)

    return wrapper_function


@app.route('/user', methods=['GET'])
@token_required
def get_users(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    users = User.query.all()
    outputs = []

    for user in users:
        output = {}
        output['uuid'] = user.uuid
        output['name'] = user.name
        output['admin'] = user.admin
        outputs.append(output)

    return jsonify({'users': outputs})


@app.route('/user/<uuid>', methods=['GET'])
@token_required
def get_one_user(current_user, uuid):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    user = User.query.filter_by(uuid=uuid).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    output = {}
    output['uuid'] = user.uuid
    output['name'] = user.name
    output['admin'] = user.admin

    return jsonify({'user': output})


@app.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})

    # get data from POST
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

    user = User(uuid=str(uuid4()), name=data['name'], password=hashed_password, admin=False)

    db.session.add(user)
    db.session.commit()

    output = {}
    output['uuid'] = user.uuid
    output['name'] = user.name
    output['admin'] = user.admin

    return jsonify({'user': output})


@app.route('/user/<uuid>', methods=['PUT'])
@token_required
def promote_user(current_user, uuid):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})
    user = User.query.filter_by(uuid=uuid).first()
    if not user:
        return jsonify({'message': 'No user found!'})

    # promote to admin
    user.admin = True

    output = {}
    output['uuid'] = user.uuid
    output['name'] = user.name
    output['admin'] = user.admin

    return jsonify({'user': output})


@app.route('/user/<uuid>', methods=['DELETE'])
@token_required
def delete_user(current_user, uuid):
    if not current_user.admin:
        return jsonify({'message': 'Cannot perform that function!'})
    user = User.query.filter_by(uuid=uuid).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': f'The user {uuid} has been deleted!'})


@app.route('/login')
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    user = User.query.filter_by(name=auth.username).first()

    if not user:
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    if not bcrypt.check_password_hash(user.password, auth.password):
        return make_response('Could not verify', 401, {'WWW-Authenticate': 'Basic realm="Login required!"'})

    token = jwt.encode({'uuid': user.uuid, 'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'], algorithm='HS256')

    return jsonify({'token': token.decode('utf-8')})


@app.route('/todo', methods=['GET'])
@token_required
def get_all_todos(current_user):
    todos = Todo.query.filter_by(user_id=current_user.id).all()

    outputs = []

    for todo in todos:
        todo_data = {}
        todo_data['id'] = todo.id
        todo_data['text'] = todo.text
        todo_data['completed'] = todo.completed
        outputs.append(todo_data)

    return jsonify({'todos': outputs})


@app.route('/todo/<todo_id>', methods=['GET'])
@token_required
def get_one_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    output = {}
    output['id'] = todo.id
    output['text'] = todo.text
    output['completed'] = todo.completed

    return jsonify({'todo': output})


@app.route('/todo', methods=['POST'])
@token_required
def create_todo(current_user):
    data = request.get_json()

    new_todo = Todo(text=data['text'], completed=False, user_id=current_user.id)
    db.session.add(new_todo)
    db.session.commit()

    todo_data = {}
    todo_data['id'] = new_todo.id
    todo_data['text'] = new_todo.text
    todo_data['completed'] = new_todo.completed

    return jsonify({'todo': todo_data})


@app.route('/todo/<todo_id>', methods=['PUT'])
@token_required
def completed_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    todo.completed = True
    db.session.commit()

    return jsonify({'message': 'Todo item has been completed!'})


@app.route('/todo/<todo_id>', methods=['DELETE'])
@token_required
def delete_todo(current_user, todo_id):
    todo = Todo.query.filter_by(id=todo_id, user_id=current_user.id).first()

    if not todo:
        return jsonify({'message': 'No todo found!'})

    db.session.delete(todo)
    db.session.commit()

    return jsonify({'message': 'Todo item deleted!'})


if __name__ == '__main__':
    app.run(debug=True)
