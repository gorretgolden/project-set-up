from flask_sqlalchemy import SQLAlchemy
from Project.db import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    residence = db.Column(db.String(30))
    age = db.Column(db.String(30))
    phoneNo = db.Column(db.String(30))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    role = db.Column(db.String(30))
    nationality = db.Column(db.String(30))
    tutor_id = db.Column(db.Integer, db.ForeignKey(
        'tutors.id'), nullable=False)

    # lets the class initialize the object's attributes
    def __init__(self, name, residence, age, phoneNo, email, password, role, nationality):
        self.name = name
        self.residence = residence
        self.age = age
        self.phoneNo = phoneNo
        self.email = email
        self.password = password
        self.role = role
        self.nationality = nationality

# Representing a class's object as a string
# F-strings provide a way to embed expressions inside string literals
    def __repr__(self):
         return "<User %r>" % self.name


# the Session establishes all conversations with the database


    def create(self):
        db.session.add(self)
        db.session.commit()
       
