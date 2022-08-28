from flask import Flask,jsonify, request, jsonify, make_response,Blueprint
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db
from Project.program.serializers import ProgramSchema

program = Blueprint('program', __name__,url_prefix="/program")



@program.route('/api/v1/program', methods=['GET'])
def getPrograms():
    get_Programs = Program.query.all()
    program_schema = ProgramSchema(many=True)
    programs = program_schema.dump(get_Programs)
    return make_response(jsonify({"programs": programs}))


@program.route('/api/v1/program/<id>', methods=['GET'])
def get_program_by_id(id):
    get_program =Program.query.get(id)
    program_schema = ProgramSchema()
    program = program_schema.dump(get_program)
    return make_response(jsonify({"program": program}))


@program.route('/api/v1/program/<id>', methods=['PUT'])
def update_program_by_id(id):
    data = request.get_json()
    get_program = Program.query.get(id)
    if data.get('program_name'):
        get_program.program_name = data['program_name']
    if data.get('time_of_schedule'):
        get_program.time_of_schedule = data['time_of_schedule']
  
    db.session.add(get_program)
    db.session.commit()
    program_schema = ProgramSchema(
        only=['id', 'program_name', 'time_of_schedule'])
    program = program_schema.dump(get_program)
    return make_response(jsonify({"program": program}))


@program.route('/api/v1/program/<int:id>', methods=['DELETE'])
def delete_program_by_id(id):
    get_Program = Program.query.filter_by(id=id)
    get_Program.deleteProgram()
    return make_response("", 204)


@program.route('/api/v1/program', methods=['POST'])
def create_program():
    data = request.get_json()
    program = Program(data['program_name'], data['time_of_schedule'])
    program.create()
    return make_response(jsonify({"program": data}), 200)
