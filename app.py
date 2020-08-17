from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from flask_cors import CORS

from os import environ

app = Flask(__name__)
CORS(app)
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] = environ.get("JWT_SECRET_KEY")
app.config['JWT_TOKEN_LOCATION'] = ('cookies', 'headers')
app.config['JWT_ACCESS_COOKIE_PATH'] = '/api/'
app.config['JWT_COOKIE_CSRF_PROTECT'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/image-storage'
}
initialize_db(app)
initialize_routes(api)

app.run()


