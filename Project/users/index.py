from flask import Flask,jsonify, request, jsonify, make_response,Blueprint
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from Project.models.user import User
from Project.models.programs import Program
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from Project.models.tutor import Tutor
from Project.db import db
from Project.users.serializers import UserSchema
users = Blueprint('users', __name__,url_prefix="/users")




@users.route('/api/v1/user', methods=['GET'])
def getUsers():
    get_Users = User.query.all()
    user_schema = UserSchema(many=True)
    users = user_schema.dump(get_Users)
    return make_response(jsonify({"users": users}))


@users.route('/api/v1/user/<id>', methods=['GET'])
def get_user_by_id(id):
    get_user = User.query.get(id)
    user_schema = UserSchema()
    user = user_schema.dump(get_user)
    return make_response(jsonify({"user": user}))


@users.route('/api/v1/user/<id>', methods=['PUT'])
def update_user_by_id(id):
    data = request.get_json()
    get_user = User.query.get(id)
    if data.get('name'):
        get_user.name = data['name']
    if data.get('residence'):
        get_user.residence = data['residence']
    if data.get('phoneNo'):
        get_user.phoneNo = data['phoneNo']
    if data.get('email'):
        get_user.email = data['email']
    if data.get('password'):
        get_user.password = data['password']
    if data.get('role'):
        get_user.role = data['role']
    if data.get('nationality '):
        get_user.nationality  = data['nationality']
    db.session.add(get_user)
    db.session.commit()
    user_schema = UserSchema(
        only=['id', 'name', 'residence', 'phoneNo', 'email', 'password','role', 'nationality'])
    user = user_schema.dump(get_user)
    return make_response(jsonify({"user": user}))


@users.route('/api/v1/user/<id>', methods=['DELETE'])
def delete_user_by_id(id):
    get_User = User.query.get(id)
    db.session.delete(get_User)
    db.session.commit()
    return make_response("", 204)


@users.route('/api/v1/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(data['name'], data['residence'],
                data['phoneNo'], data['email'], data['password'],data['role'], data['nationality'])
    user.create()
    return make_response(jsonify({"user": data}), 200)

@users.route('/api/v1/user/checkin', methods=['POST'])
def checkUsernameAndPassword():
    data = request.get_json()
    username = data['name']
    password = data['password']
    get_user = User.query.filter_by(name=username).first()
    if get_user.password == password:
        user_schema = UserSchema(
            only=['id', 'name', 'residence', 'phoneNo', 'email', 'password','role', 'nationality'])
        user = user_schema.dump(get_user)
        return make_response(jsonify({"user": user}))

    return make_response("Failure", 403)

