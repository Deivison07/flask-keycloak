from cachelib import SimpleCache
from keycloak import KeycloakOpenID
from auth.keycloak import KeycloakClient

from common.settings import (KEYCLOAK_client_id, 
                             KEYCLOAK_client_secret_key, 
                             KEYCLOAK_realm_name, 
                             KEYCLOAK_server_url, 
                             )


keycloak_openid_instance = KeycloakOpenID(
                                    server_url          =   KEYCLOAK_server_url,
                                    client_id           =   KEYCLOAK_client_id,
                                    realm_name          =   KEYCLOAK_realm_name,
                                    client_secret_key   =   KEYCLOAK_client_secret_key
                                )

cache = SimpleCache(threshold=10 ,default_timeout=180)
keycloak_openid = KeycloakClient(keycloak_openid_instance, cache) 

