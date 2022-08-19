import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

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

    def encode_token(self, user_id):
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

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.JWT_SECRET, self.JWT_ALGORITHM)
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return False
        except jwt.InvalidTokenError as e:
            return False