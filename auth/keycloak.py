# Configuração para ajustar o Audience no keycloak
#
# Clients > Your client > Client scopes > your-client-dedicated > Add mapper > by configuration > Audience.
# Add a name of the mapper, select your client on the select box and enable "Add to access token".
# Your client should now be in the "aud" field of the access token

from cachetools import TTLCache
from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakError, KeycloakAuthenticationError, KeycloakAuthorizationConfigError
from requests import request

class KeycloakClient():
    def __init__(self, keycloak: KeycloakOpenID, cache: TTLCache, cacheActive=True) -> None:

        #KeycloakOpenID
        if isinstance(keycloak,KeycloakOpenID):
            self.keycloak: KeycloakOpenID = keycloak
        else:
            raise KeycloakError()
        
        self.cache : TTLCache =  cache

        self.cacheActive = cacheActive
    
    def _inCache(self, token_id:str) -> dict|bool:
        if self.cacheActive == False:
            return None

        cache = self.cache.get(token_id)
        if cache:
            return cache 
        return None

    def _setCache(self, token_id: str|int, body:any) -> None:
        self.cache.set(token_id, body)

    def _is_valid(self, request: request) -> dict|bool:

        token = str(request.headers.get('Authorization')).removeprefix('Bearer ')
        if not token:
            raise KeycloakAuthenticationError("autenticação necessaria")
        
        #verifica se a chave publica está em cache
        pk = self._inCache('public_key')
        if pk is None:
            pk = self.public_key()
        
        #decodifica o token para descobrir o JTI
        token_id = self.keycloak.decode_token(token, pk)['jti']

        # veifica se o profile referente ao token está em cache
        prof = self._inCache(token_id)
        if prof is not None:
            return prof 

        # Busca o profile caso o mesmo não esteja em cache
        profile : dict = self.keycloak.introspect(token=token)
        if profile['active'] != True:
            return False
        
        self._setCache(token_id, profile)
        return profile

    def public_key(self):
        #PEM key
        pk = f"-----BEGIN PUBLIC KEY-----\n{self.keycloak.public_key()}\n-----END PUBLIC KEY-----"
        self._setCache('public_key', pk)
        return pk
        

    def get_credentials_token(self) -> dict:
        return self.keycloak.token(grant_type='client_credentials')
    
    def _role_in_client(self, role: str, request: request) -> bool:

        rolesList = self._is_valid(request=request)['resource_access'][self.keycloak.client_id]["roles"]
        if role in rolesList:
            return True
        return False
    
    def is_valid(self, request:request):
        def decorator(funcao):
            def wrapper(*args, **kwargs):
                if self._is_valid(request):
                     return funcao(*args, **kwargs)
                raise KeycloakAuthenticationError("Erro ao autenticar token")
            return wrapper
        return decorator
    
    def role_in_client(self, role: str, request:request):
        def decorator(func):
            def wrapper(*args, **kwargs):
                if self._role_in_client(role, request):
                    return func(*args, **kwargs)
                raise KeycloakAuthorizationConfigError("Erro token não está autorizado para esta rotina")
            return wrapper
        return decorator
    



    
    

    
