from flask import Flask
from flask_migrate import Migrate
from models import db
from routes.api.UserRoute import user_route
from routes.api.AuthRoute import auth_route

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)
migrate = Migrate(app, db)

### ROUTE API ###
app.register_blueprint(auth_route, url_prefix='/api/auth')
app.register_blueprint(user_route, url_prefix='/api/users')


### ROUTE WEB ###

if __name__ == '__main__':
    app.debug = True
    app.run()