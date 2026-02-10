import os
import unittest

from turboapi.authenticator import Authenticator

class LoginTestCase(unittest.TestCase):

    def test_login(self):

        turbo=os.getenv('TURBO_URL')
        authenticator: Authenticator = Authenticator(turbo)

        username = os.getenv('TURBO_USERNAME')
        password = os.getenv('TURBO_PASSWORD')
        token_key, token = authenticator.login(username, password)

        self.assertIsNotNone(token)

if __name__ == '__main__':
    unittest.main()
