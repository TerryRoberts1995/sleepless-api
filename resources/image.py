from flask import Response, request
from database.models import Image
from flask_restful import Resource

# Gallery is going to keep list of images for the gallery.
class ImagesApi(Resource):
    def get(self):
        images = Image.objects().to_json()
        return Response(images, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        image =  Image(**body).save()
        id = image.id
        return {'id': str(id)}, 200
        
class ImageApi(Resource):
    def put(self, id):
        body = request.get_json()
        Image.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        image = Image.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        images = Image.objects.get(id=id).to_json()
        return Response(images, mimetype="application/json", status=200)