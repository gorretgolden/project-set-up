from flask import Flask,jsonify, request, jsonify, make_response,Blueprint
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db
from Project.tutors.serializers import TutorSchema


tutors = Blueprint('tutors', __name__,url_prefix="/tutors")



@tutors.route('/api/v1/tutor', methods=['GET'])
def getTutors():
    get_Tutors = Tutor.query.all()
    tutor_schema = TutorSchema(many=True)
    tutors = tutor_schema.dump(get_Tutors)
    return make_response(jsonify({"tutors": tutors}))


@tutors.route('/api/v1/tutor/<id>', methods=['GET'])
def get_tutor_by_id(id):
    get_tutor =Tutor.query.get(id)
    tutor_schema = TutorSchema()
    tutor = tutor_schema.dump(get_tutor)
    return make_response(jsonify({"tutor": tutor}))


@tutors.route('/api/v1/tutor/<id>', methods=['PUT'])
def update_tutor_by_id(id):
    
    data = request.get_json()
    get_tutor = Tutor.query.get(id)
   
    if data.get('tutor_name'):
        get_tutor.tutor_name = data['tutor_name']
    if data.get('notes'):
        get_tutor.notes = data['notes']

    if data.get('results'):
        get_tutor.results = data['results']
  
    db.session.add(get_tutor)
    db.session.commit()
    tutor_schema = TutorSchema(
        only=['id', 'tutor_name', 'notes','results'])
    tutor = tutor_schema.dump(get_tutor)
    return make_response(jsonify({"tutor": tutor}))


@tutors.route('/api/v1/tutor/<id>', methods=['DELETE'])
def delete_tutor_by_id(id):
    get_Tutor = Tutor.query.get(id)
    db.session.delete(get_Tutor)
    db.session.commit()
    return make_response("", 204)


@tutors.route('/api/v1/tutor', methods=['POST'])
def create_tutor():
    data = request.get_json()

    tutor = Tutor(data['name'], data['notes'], data['results'])
    tutor.create()
    return make_response(jsonify({"tutor": data}), 200)

