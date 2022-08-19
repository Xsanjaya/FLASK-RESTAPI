import json
from flask import request
from models.User import User
from models import db
from utils.auth_handler import AuthHandler

auth_handler = AuthHandler()


def login():
    req = request.json
    email    = req['email']
    password = req['password']
   
    user =  db.session.query(User).filter(User.email == email).first()

    if (user is None) or (not auth_handler.verify_password(password, user.password)):
        result = {
            "success" : False,
            "message" : "Email is Taken",
            "data"    : []
        }
        return json.dumps(result)

    token = auth_handler.encode_token(user.email)
    result = {
            "success" : True,
            "message" : "Login Success",
            "data"    : {
                'profile' : user.serialize(), 
                'token'   : token}
        }
    return json.dumps(result)


def logout():
    pass