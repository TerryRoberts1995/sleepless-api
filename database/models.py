from .db import db

class Image(db.Document):
    url = db.StringField(required=True, unique=True)
    name = db.StringField(required = True)
    