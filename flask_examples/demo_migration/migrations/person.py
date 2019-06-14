# from flask_examples import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

person_jobs = db.Table('jobs',
                       db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
                       db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
                       )


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    pets = db.relationship('Pet', backref='owner', lazy=True)  # one-to-many relationship
    jobs = db.relationship('Job', secondary=person_jobs, lazy=True, backref=db.backref('people', lazy=True))
    father = db.relationship('Parent', backref='child', lazy=True, uselist=False)


class Job(db.Model):  # many-to-many
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Pet(db.Model):  # one-to-many
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)


class Parent(db.Model):  # one-to-one
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    child_id = db.Column(db.Integer, db.ForeignKey('person.id'))
