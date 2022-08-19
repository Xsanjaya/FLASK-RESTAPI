from lib2to3.pgen2 import token
from flask import redirect, url_for, request, abort
from flask import jsonify
from models.User import User
from models import db
from utils.helpers import dict_helper
from utils.jwt_handler import AuthHandler

auth = AuthHandler()

def index():
    users = db.session.query(User).all()
    result = {
        "success" : True,
        "message" : "User All",
        "data"    : [dict_helper(users)]
    }
    return jsonify(result)


def store():
    req = request.json
    name     = req['name']
    email    = req['email']
    password = auth.hash_password( req['password'] )
    token    = auth.encode_token(email)

    user = User(name=name, email=email, password=password, token=token)
    
    db.session.add(user)
    db.session.commit()

    return user


def show(userId):
    return 'success'


def update(userId):
    return 'success'


def destroy(userId):
    return 'success'