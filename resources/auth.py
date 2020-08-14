from flask import Response,redirect, request, redirect, make_response
from flask_jwt_extended import (JWTManager, jwt_required,  
                                 get_jwt_identity, create_access_token, 
                                 create_refresh_token, set_access_cookies,
                                 set_refresh_cookies
                                 )
from database.models import User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
 def post(self):
   body = request.get_json()
   user = User(**body)
   user.hash_password()
   user.save()
   id = user.id
   return {'id': str(id)}, 200


class LoginApi(Resource):
 def post(self):
   body = request.get_json()
   user = User.objects.get(email=body.get('email'))
   authorized = user.check_password(body.get('password'))
   if not authorized:
     return {'error': 'Email or password invalid'}, 401
 
   expires = datetime.timedelta(days=7)
   access_token = create_access_token(identity=str(user.id), expires_delta=expires)
   refresh_token = create_refresh_token(identity=str(user.id))
   resp = make_response({'login' : True})
   set_access_cookies(resp, access_token)
   set_refresh_cookies(resp, refresh_token)

   return {"token" : access_token }, 200

