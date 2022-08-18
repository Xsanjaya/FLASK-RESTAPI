import sys
from flask import render_template, redirect, url_for, request, abort
from models.User import User
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def index():
    return 'success'

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