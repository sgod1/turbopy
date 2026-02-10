from turboapi.authenticator import Authenticator
from turboapi.turbo_api import TurboAPI

class TurboAuditFactory(TurboAPI):
    def __init__(self, authenticator: Authenticator) -> None:
        super().__init__(authenticator)

    def get_audit_logs(self):
        r = self.get('admin/auditlogs', 'application/zip')
        return r.content