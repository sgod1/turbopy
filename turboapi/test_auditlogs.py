import os
import unittest

from turboapi.auditlogs import TurboAuditFactory
from turboapi.authenticator import Authenticator, AuthTokenKey


class AuditCase(unittest.TestCase):

    @staticmethod
    def test_get_audit_logs():

        turbo = os.getenv('TURBO_URL')
        auth = Authenticator(turbo)

        token = auth.login(username=os.getenv('TURBO_USERNAME'), password=os.getenv('TURBO_PASSWORD'))
        sessid = token[1].split('=')[1]

        auth.set_token(AuthTokenKey.JSESSIONID,sessid)

        auditlog_factory: TurboAuditFactory = TurboAuditFactory(auth)
        auditlogzip = auditlog_factory.get_audit_logs()

        with open('/tmp/auditlogs.zip', 'wb') as f:
            f.write(auditlogzip)

if __name__ == '__main__':
    unittest.main()
