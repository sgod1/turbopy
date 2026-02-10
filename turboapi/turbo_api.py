import requests

from turboapi.authenticator import Authenticator

class TurboAPI:
    def __init__(self, authenticator: Authenticator) -> None:
        self.authenticator = authenticator

    def get_turbo_endpoint(self) -> str:
        return self.authenticator.get_turbo_endpoint()

    def get_rest_endpoint(self) -> str:
        return f"{self.get_turbo_endpoint()}/vmturbo/rest"

    def get_api_endpoint(self) -> str:
        return self.authenticator.get_api_endpoint()

    def get(self, url_segment:str, content_type=None) -> requests.Response:

        token_key, token = self.authenticator.get_token()
        url= f"{self.get_rest_endpoint()}/{url_segment}"

        accept = "application/json" if content_type is None else content_type

        r = requests.get(url, verify=False, headers={'Accept': accept}, cookies={token_key: token})
        return r

    def post(self, url_segment:str, content_type=None) -> requests.Response:
        # todo
        r = requests.post(f"{self.get_rest_endpoint()}/{url_segment}", verify=False, headers={'Accept': content_type})
        return r