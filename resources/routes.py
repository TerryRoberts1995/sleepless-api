from .image import ImagesApi, ImageApi

def initialize_routes(api):
 api.add_resource(ImagesApi, '/images')
 api.add_resource(ImageApi, '/images/<id>')