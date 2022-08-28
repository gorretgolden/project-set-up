from flask_sqlalchemy import SQLAlchemy
from Project.db import db


class CourseUnit(db.Model):
    __tablename__ = "course_units"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    program_id = db.Column(db.Integer, db.ForeignKey('programs.id'), nullable=False)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutors.id'), nullable=False)

    def __init__(self, course_unit_name, programs_id):
        self.course_unit_name = course_unit_name
        self.programs_id = programs_id

    def __repr__(self):
        return "<CourseUnit %r>" % self.name


    def create(self):
        db.session.add(self)
        db.session.commit()
      