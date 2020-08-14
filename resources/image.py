from flask import Response, request
from database.models import Image, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

# Gallery is going to keep list of images for the gallery.
class ImagesApi(Resource):
    def get(self):
        user_id = get_jwt_identity()
        images = Image.objects().to_json()
        return Response(images, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        image = Image(**body, added_by=user)
        image.save()
        user.update(push__images=image)
        user.save()
        id = image.id
        return {'id': str(id)}, 200
    
    # def delete(self): clean MOCK data. 
    #     images = Image.objects.delete()
    #     return '', 200

class ImageApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        image = Image.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Image.objects.get(id=id).update(**body)
        return '', 200
    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        image = Image.objects.get(id=id, added_by=user_id)
        image.delete()
        return '', 200

    def get(self, id):
        images = Image.objects.get(id=id).to_json()
        return Response(images, mimetype="application/json", status=200)