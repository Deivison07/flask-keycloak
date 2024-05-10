from flask import Flask
from common.database import config_database
from routers.routers import register_routes

app = Flask(__name__) #app

config_database(app) 

register_routes(app) 

# app.before_request() #middleware autencication

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)