from flask_sqlalchemy import SQLAlchemy
from Project.db import db


class Program(db.Model):
    __tablename__ = "programs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    time_of_schedule = db.Column(db.String)
    customer_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self, name, time_of_schedule, customer_id):
        self.name = name
        self.time_of_schedule = time_of_schedule
        self.customer_id = customer_id

    def __repr__(self):
        return "<Program %r>" % self.name


    def create(self):
        db.session.add(self)
        db.session.commit()
        



    def deleteProgram(self):
        db.session.delete(self)
        db.session.commit()