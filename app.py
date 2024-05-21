from flask import Flask, jsonify, request
from common.database import config_database
from common.initial import keycloak_openid
from jwcrypto.jwt import JWTExpired

from routers.routers import register_routes

app = Flask(__name__)   #instancia Flask app

config_database(app)    #banco de dados
register_routes(app)    #rotas 

@app.before_request
def autentication():
   try:
      if not keycloak_openid._is_valid(request):
         return jsonify({'error':'Falha na autenticação'}), 401
       
   except JWTExpired:
      return jsonify({'error':'Token expirado'}), 401
   
   except Exception as e:
      return jsonify({'error': e}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)