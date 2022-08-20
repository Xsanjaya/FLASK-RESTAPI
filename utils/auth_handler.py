import json
from flask import request, make_response
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from functools import wraps

from models.User import User

from config import JWT_ALGORITHM, JWT_SECRET


class AuthHandler():
    pwd_context     = CryptContext(schemes=["bcrypt"], deprecated="auto")
    # JWT_SECRET      = config.JWT_SECRET
    # JWT_ALGORITHM   = config.JWT_ALGORITHM 
    JWT_SECRET      = JWT_SECRET
    JWT_ALGORITHM   = JWT_ALGORITHM 

    def hash_password(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def token_encode(self, user_id):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=5),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            self.JWT_SECRET,
            self.JWT_ALGORITHM
        )

    def token_decode(self, token):
        try:
            payload = jwt.decode(token, self.JWT_SECRET, self.JWT_ALGORITHM)
            return payload['sub']

        except jwt.ExpiredSignatureError as e:
            return False

        except jwt.InvalidTokenError as e:
            return False

    def auth_wrapper(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'x-token' in request.headers:
                token = request.headers['x-token']
            if not token:
                return json.dumps({'message' : str(request.headers)})
    
            try:
                data = jwt.decode(token, self.JWT_SECRET, self.JWT_ALGORITHM)['sub']
                print(data)
                current_user = User.query.filter_by(token=data).first()
            except Exception as e:
                return json.dumps({
                    'message' : 'Token is invalid !!',
                    'error'   : str(e)
                })
            # returns the current logged in users contex to the routes
            return  f(current_user, *args, **kwargs)

        return decorated