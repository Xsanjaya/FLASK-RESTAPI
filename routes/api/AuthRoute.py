from flask import Blueprint
from controllers.api.AuthController import login, logout

auth_route = Blueprint('auth_route', __name__)

auth_route.route('/login', methods=['POST'])(login)
auth_route.route('/logout', methods=['GET'])(logout)
