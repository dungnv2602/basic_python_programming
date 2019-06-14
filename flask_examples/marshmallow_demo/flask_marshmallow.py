from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo_marshmallow.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    rewards = db.relationship('Reward', backref='owner', lazy=True)


class Reward(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reward_name = db.Column(db.String(100), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
    rewards = ma.List(ma.HyperlinkRelated('rewards'))


class RewardSchema(ma.ModelSchema):
    class Meta:
        model = Reward
    owner = ma.HyperlinkRelated('users')


@app.route('/users')
def users():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    return jsonify({'users': output.data})


@app.route('/rewards')
def rewards():
    rewards = Reward.query.all()
    reward_schema = RewardSchema(many=True)
    output = reward_schema.dump(rewards)
    return jsonify({'rewards': output.data})


if __name__ == '__main__':
    app.run(debug=True)
