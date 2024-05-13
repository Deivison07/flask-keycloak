import os
from dotenv import load_dotenv
from flask import Flask
from keycloak import KeycloakOpenID
from cachetools import TTLCache
from flask_caching import Cache

from auth.keycloak import KeycloakClient

load_dotenv()

# Configurações de banco de dados
database_host = os.getenv("DATABASE_IP",'127.0.0.1')
database_pass = os.getenv("DATABASE_PASS")
database_port = os.getenv("DATABASE_PORT")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("DATABASE_USER")
DATABASE_CONNECTION_URL = f"postgresql://{database_user}:{database_pass}@{database_host}:{database_port}/{database_name}"

# Configurações keycloak (autenticação e autorização)
KEYCLOAK_server_url = os.getenv("KEYCLOAK_server_url")
KEYCLOAK_client_id = os.getenv("KEYCLOAK_client_id")
KEYCLOAK_client_secret_key = os.getenv("KEYCLOAK_client_secret_key")
KEYCLOAK_realm_name = os.getenv("KEYCLOAK_realm_name")

keycloak_openid = KeycloakOpenID(
                                    server_url          =   KEYCLOAK_server_url,
                                    client_id           =   KEYCLOAK_client_id,
                                    realm_name          =   KEYCLOAK_realm_name,
                                    client_secret_key   =   KEYCLOAK_client_secret_key
                                )



def config_auth(app: Flask):
    app.config['CACHE_TYPE'] = 'simple'  # Use 'simple' para cache em memória
    app.config['CACHE_DEFAULT_TIMEOUT'] = 180  # Tempo de vida padrão
    app.config['CACHE_THRESHOLD'] = 10  # Tamanho máximo do cache
    
    cache = Cache(app)
    app.auth = KeycloakClient(keycloak_openid, cache)

