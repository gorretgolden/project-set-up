from flask import Flask,jsonify, request, jsonify, make_response,Blueprint
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.courseUnit import CourseUnit
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db
from Project.courseUnits.serializers import CourseUnitSchema
courseUnits = Blueprint('courseUnits', __name__)


@courseUnits.route('/api/v1/courseUnits', methods=['GET'])
def getTutors():
    get_CourseUnits = CourseUnit.query.all()
    courseUnit_schema = CourseUnitSchema(many=True)
    courseUnits =courseUnit_schema.dump(get_CourseUnits)
    return make_response(jsonify({"courseUnits": courseUnits}))


@courseUnits.route('/api/v1/courseUnit/<id>', methods=['GET'])
def get_courseUnit_by_id(id):
    get_courseUnit =CourseUnit.query.get(id)
    courseUnit_schema = CourseUnitSchema()
    courseUnit = courseUnit_schema.dump(get_courseUnit)
    return make_response(jsonify({"courseUnit": courseUnit}))


@courseUnits.route('/api/v1/courseUnit/<id>', methods=['PUT'])
def update_courseUnit_by_id(id):
    data = request.get_json()
    get_courseUnit = CourseUnit.query.get(id)
    if data.get('course_unit_name'):
        get_courseUnit.course_unit_name = data['course_unit_name']

    db.session.add(get_courseUnit)
    db.session.commit()
    courseUnit_schema = CourseUnitSchema(
        only=['id', 'course_unit_name'])
    courseUnit = courseUnit_schema.dump(get_courseUnit)
    return make_response(jsonify({"courseUnit": courseUnit}))


@courseUnits.route('/api/v1/courseUnit/<id>', methods=['DELETE'])
def delete_courseUnit_by_id(id):
    get_CourseUnit = CourseUnit.query.get(id)
    db.session.delete(get_CourseUnit)
    db.session.commit()
    return make_response("", 204)


@courseUnits.route('/api/v1/courseUnit', methods=['POST'])
def create_courseUnit():
    data = request.get_json()
    courseUnit = CourseUnit(data['course_unit_name'])
    courseUnit.create()
    return make_response(jsonify({"courseUnit": data}), 200)

