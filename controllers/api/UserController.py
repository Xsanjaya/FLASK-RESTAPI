from flask import redirect, url_for, request, abort
from flask import jsonify
from models.User import User
from models import db
from utils import hashing
from utils.helpers import dict_helper
from utils.auth_handler import AuthHandler

auth = AuthHandler()

def index():
    users = db.session.query(User).all()
    result = {
        "success" : True,
        "message" : "User All",
        "data"    : [dict_helper(users)]
    }
    return jsonify(result)


def register():
    req = request.json
    name     = req['name']
    email    = req['email']
    password = auth.hash_password( req['password'] )
    token    = hashing(email)

    try:
        user = User(name=name, email=email, password=password, token=token)
        
        db.session.add(user)
        db.session.commit()

        result = {
            "success" : True,
            "message" : "Create User",
            "data"    : [user.serialize()]
        }

    except Exception as err:
        result = {
            "success" : False,
            "message" : "Create User Error",
            "data"    : [str(err)]
        }

    return jsonify(result)


def show(userId):
    return 'success'


def update(userId):
    return 'success'


def destroy(userId):
    return 'success'