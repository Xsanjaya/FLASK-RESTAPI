from passlib.context import CryptContext

pwd_context  = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing(self, text):
    return self.pwd_context.hash(text)