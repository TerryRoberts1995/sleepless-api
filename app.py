from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes
from os import environ

app = Flask(__name__)


app.config['ENV_FILE_LOCATION'] = environ.get('JWT_SECRET_KEY')
api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/image-storage'
}
initialize_db(app)
initialize_routes(api)

app.run()


