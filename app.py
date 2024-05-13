from flask import Flask, jsonify
from flask import request
from common.database import config_database
from routers.routers import register_routes
from common.settings import config_auth
from keycloak.exceptions import KeycloakError, KeycloakAuthenticationError, KeycloakAuthorizationConfigError
from jwcrypto.jwt import JWTExpired

app = Flask(__name__) #app

config_database(app) 
register_routes(app) 
config_auth(app)


@app.before_request
def autentication():
   try:
    app.auth._is_valid(request)
   except JWTExpired as eJWT:
      return jsonify({'error':'Token expirado'}), 401
   
   except Exception as e:
      return jsonify({'error': e.error_message}), 401


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)