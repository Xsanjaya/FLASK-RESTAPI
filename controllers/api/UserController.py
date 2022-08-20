import json
from flask import request
from flask_login import current_user, login_required
from models.User import User
from models import db
from utils.auth_handler import AuthHandler

auth = AuthHandler()

@auth.auth_wrapper
def index():
    users = db.session.query(User).all()
    
    result = {
        "success" : True,
        "message" : "User All",
        "data"    : [ dict(user.list()) for user in users ]
    }
    return json.dumps(result)


@login_required
def show(userId):
    if current_user.is_authenticated:
        resp = {"result": 200,
                "data": current_user.to_json()}
    else:                                                                                                                    
        resp = {"result": 401,
                "data": {"message": "user no login"}}

    return json.dumps(resp)

def update(userId):
    return 'success'


def destroy(userId):
    return 'success'