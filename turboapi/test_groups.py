import unittest
import os

from turboapi.authenticator import Authenticator, AuthTokenKey
from turboapi.groups import TurboGroup, GroupFactory


class GroupsCase(unittest.TestCase):

    def authenticate(self) -> Authenticator:
        turbo = os.getenv('TURBO_URL')
        auth = Authenticator(turbo)

        token = auth.login(username=os.getenv('TURBO_USERNAME'), password=os.getenv('TURBO_PASSWORD'))
        sessid = token[1].split('=')[1]

        auth.set_token(AuthTokenKey.JSESSIONID,sessid)
        return auth

    def test_list_groups(self):
        auth = self.authenticate()

        group_factory: GroupFactory = GroupFactory(auth)
        gs: list[TurboGroup] = group_factory.list_groups()

        for group in gs:
            print(group.__dict__)

        g = gs[0]
        group_factory.list_group_actions(g.uuid)

    def test_list_groups_by_group_type(self):
        auth = self.authenticate()

        group_factory: GroupFactory = GroupFactory(auth)

        group_type = "ContainerSpec"
        is_static = False

        gs: list[TurboGroup] = group_factory.list_groups_by_group_type(group_type, is_static)

        print("container spec groups:")

        for group in gs:
            print(group.__dict__)

        group_type = "WorkloadController"
        gs: list[TurboGroup] = group_factory.list_groups_by_group_type(group_type, is_static)

        print("workload controller groups:")

        for group in gs:
            print(group.__dict__)

        print("criteria list:")

        for group in gs:
            print(group.criteriaList)

        # g = gs[0]
        # group_factory.list_group_actions(g.uuid)

if __name__ == '__main__':
    unittest.main()
