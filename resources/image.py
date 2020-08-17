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

    
    def post(self):
        body = request.form
        image = Image(**body)
        image.save()
        id = image.id
        return {'id': str(id)}, 200
    
    # def delete(self): clean MOCK data. 
    #     images = Image.objects.delete()
    #     return '', 200

class ImageApi(Resource):
    
    def put(self, id):
        
        image = Image.objects.get(id=id)
        body = request.get_json()
        Image.objects.get(id=id).update(**body)
        return '', 200
   
    def delete(self, id):
        
        image = Image.objects.get(id=id)
        image.delete()
        return '', 200

    def get(self, id):
        images = Image.objects.get(id=id).to_json()
        return Response(images, mimetype="application/json", status=200)