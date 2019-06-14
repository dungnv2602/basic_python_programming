# from flask_examples import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

person_jobs = db.Table('jobs',
                       db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
                       db.Column('person_id', db.Integer, db.ForeignKey('person.id'), primary_key=True)
                       )


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    jobs = db.relationship('Job', secondary=person_jobs, lazy=True, backref=db.backref('people', lazy=True))
    pets = db.relationship('Pet', backref='owner', lazy=True)  # one-to-many relationship
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


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///person.db'

db.init_app(app)

app.app_context().push()

j1 = Job.query.filter_by(id=21).first_or_404()
for person in j1.people:
    print(person.name)


# update all
updated = Person.query.filter_by(name='Nguyen Dung 1').update({Person.name: 'Updated'})
print(updated)
db.session.commit()


# delete all
deleted = Person.query.filter_by(name='Updated').delete()
print(deleted)
db.session.commit()

# order by
Member.query.order_by(Member.id).limit(2).all()
Member.query.filter(db._or(Member.username == 'Anthony', Member.username == 'Karl')).order_by(Member.id).all()

# offset --> skip to the index
# skip first index
Member.query.offset(1).all()
# skip first 3 indexes
Member.query.offset(3).all()
# skipp first 2 --> limit to 5 result
Member.query.offset(2).limit(5).all()
Member.query.order_by(Member.id.desc()).offset(2).first()

# outerjoin
db.session.query(Customer, Purchase).outerjoin(Purchase, Customer.id == Purchase.customer_id).all()
db.session.query(Customer.name, Purchase.price).outerjoin(Purchase, Customer.id == Purchase.customer_id).all()

# join group by count
db.session.query(Customer.name, db.func.count(Purchase.customer_id)).outerjoin(Purchase, Customer.id == Purchase.customer_id).group_by(Customer.name).all()

# join group by sum
db.session.query(Customer.name, db.func.sum(Purchase.price)).outerjoin(Purchase, Customer.id == Purchase.customer_id).group_by(Customer.name).all()
