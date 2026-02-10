from enum import StrEnum

import requests

class AuthTokenKey(StrEnum):
    JSESSIONID = 'JSESSIONID'

class Authenticator:

    def __init__(self, turbo_endpoint: str):
        self.turbo_endpoint = turbo_endpoint
        self.token_key: str | None = None
        self.token: str|None = None

    def set_token(self, token_key:str, token:str):
        self.token_key = token_key
        self.token = token

    def get_token(self) -> (str, str):
        return self.token_key, self.token

    def import_token_from_file(self, file) -> str|None:
        pass

    def get_turbo_endpoint(self) -> str:
        return self.turbo_endpoint

    def get_api_endpoint(self) -> str:
        return f"{self.get_turbo_endpoint()}/api/v3"

    def login(self, username:str, password:str) -> (str|None, str|None):

        url = f'{self.get_api_endpoint()}/login?hateoas=true'
        data = {'username': username, 'password': password}

        # data is x-www-url-encoded form
        data = f'username={username}&password={password}'

        #h={'Content-Type': 'application/x-www-form-urlencoded'}

        response: requests.Response = requests.post(url, headers={'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}, data=data.encode('utf-8'), verify=False)
        rh = response.headers
        print(rh)
        self.token_key= AuthTokenKey.JSESSIONID
        self.token = rh['set-cookie'].split(';')[0]
        return self.token_key, self.token
