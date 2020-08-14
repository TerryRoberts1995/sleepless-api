from .image import ImagesApi, ImageApi
from .user import UserApi, DeleteUserApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
 api.add_resource(ImagesApi, '/images')
 api.add_resource(ImageApi, '/images/<id>')
 api.add_resource(SignupApi, '/api/auth/signup')
 api.add_resource(LoginApi, '/api/auth/login')
 api.add_resource(UserApi, '/users')
 api.add_resource(DeleteUserApi, '/users/<id>')

 