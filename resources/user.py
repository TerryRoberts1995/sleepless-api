from flask import Response, request
from database.models import User
from flask_restful import Resource


class UserApi(Resource):
    def get(self):
        users = User.objects().to_json()
        return Response(users, mimetype="application/json", status=200)

class DeleteUserApi(Resource):
    def delete(self, id):
        user = User.objects.get(id=id)
        user.delete()
        return 'deleted', 200