from flask import render_template, redirect, url_for, request, abort
from flask import jsonify
from models.User import User
from models import db

def index():
    # users = db.session.all()
    result = {
        "success" : True,
        "message" : "User All",
        "data"    : []
    }
    return jsonify(result)

def register():
    return 'success'


def store():
    return 'success'


def show(userId):
    return 'success'


def update(userId):
    return 'success'


def destroy(userId):
    return 'success'