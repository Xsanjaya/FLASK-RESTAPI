from models import db

class User(db.Model):
    __tablename__ = 'users'

    id 			= db.Column('id', db.Integer, primary_key=True)
    name		= db.Column('name', db.String)
    email		= db.Column('email', db.String, unique=True)
    password	= db.Column('password', db.String)
    token       = db.Column('token', db.String)
    created_at 	= db.Column('created_at', db.DateTime, default=db.func.NOW())
    updated_at 	= db.Column('updated_at', db.DateTime, default=db.func.NOW(), onupdate=db.func.NOW())

    @property
    def serialize(self):
        return {
            'id'    : self.id,
            'name'  : self.name,
            'email'     : self.city,
            'password'  : self.state,
            'token'     : self.address
        }