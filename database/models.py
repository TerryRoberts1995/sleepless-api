from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class Image(db.Document):
    url = db.StringField(required=True, unique=True)
    name = db.StringField(required = True)
    added_by = db.ReferenceField('User')

class User(db.Document):
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    images = db.ListField(db.ReferenceField('Image', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(Image, 'added_by', db.CASCADE)
    