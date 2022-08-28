from flask_sqlalchemy import SQLAlchemy
from Project.db import db

class Tutor(db.Model):
    __tablename__ = "tutors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    notes = db.Column(db.String(225))
    results = db.Column(db.String(25))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __init__(self,id,name,notes,results,user_id):
        self.name = name
        self.notes = notes
        self.results = results
        self.user_id= user_id
       

    def __repr__(self):
         return "<Tutor %r>" % self.name

    def create(self):
        db.session.add(self)
        db.session.commit()
  

 

