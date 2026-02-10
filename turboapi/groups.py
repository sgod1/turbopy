from enum import StrEnum, verify
from typing import List

from turboapi.authenticator import Authenticator
from turboapi.turbo_api import TurboAPI

class LogicalOperators(StrEnum):
    AND = 'AND'
    OR = 'OR'

class SourceType(StrEnum):
    KUBERNETES = "Kubernetes"

class Origin(StrEnum):
    DISCOVERED = "Discovered"

class Source:
    def __init__(self, source_type: SourceType) -> None:
        self.uuid: str = ""
        self.displayName: str = ""
        self.category: str = ""
        self.isProbeRegistered: bool = False
        self.type: SourceType = source_type
        self.readOnly: bool = False

class TurboGroup:
    def __init__(self, **kwargs) -> None:

        self.uuid: str = ""
        self.displayName: str = ""
        self.className: str = ""
        self.membersCount: int = 0
        self.entitiesCount: int = 0
        self.groupType: str = ""
        self.severity: str = ""
        self.environmentType: str=""
        self.isStatic: bool=False
        self.logicalOperator: str=LogicalOperators.AND
        self.memberUuidList: List[str] = []
        self.temporary: bool=False
        self.activeEntitiesCount: int=0
        self.cloudType: str=""
        self.source: Source=Source(source_type=SourceType.KUBERNETES)
        self.memberTypes: List[str] = []
        self.groupOrigin: Origin = Origin.DISCOVERED
        self.groupClassName: str=""
        self.criteriaList: List[dict] = []

class GroupFactory(TurboAPI):

    def __init__(self, authenticator: Authenticator) -> None:
        super().__init__(authenticator)

    def list_groups(self) -> List[TurboGroup] | None:
        r = self.get('groups')

        group_list: List[TurboGroup] = []

        # r.json() is a list of groups
        gs = r.json()

        for g in gs:
            tg: TurboGroup = TurboGroup()

            #print(g.keys())

            # dict_keys(['uuid', 'displayName', 'className', 'membersCount', 'entitiesCount',
            # 'groupType', 'severity', 'environmentType', 'isStatic', 'logicalOperator',
            # 'memberUuidList', 'temporary', 'activeEntitiesCount', 'cloudType', 'source',
            # 'memberTypes', 'entityTypes', 'groupOrigin', 'groupClassName', 'criteriaList'])

            for k in g.keys():
                tg.__dict__[k] = g[k]

            group_list.append(tg)

        return group_list

    def list_groups_by_group_type(self, group_type: str, is_static: bool = True) -> List[TurboGroup] | None:
        gs = self.list_groups()

        gs1 = [g for g in gs if g.groupType == group_type and g.isStatic == is_static]

        return gs1

    def list_group_actions(self, group_uuid: str) -> List[TurboGroup] | None:

        url = f'groups/{group_uuid}/actions?ascending=true&forceExpansionOfAggregatedEntities=false'
        r = self.get(url)

        # list of actions
        actions = r.json()

        for a in actions:
            print(a)

    def delete_group(self, group_uuid: str) -> None:
        pass

    def create_group_one_member(self, group_name: str, **kwargs) -> TurboGroup:
        # create group, pass member entity id
        pass

    def create_group_container_specs(self, group_name: str, **kwargs) -> List[TurboGroup]:
        pass

    def update_group_container_specs(self, group_name: str, **kwargs) -> List[TurboGroup]:
        pass

    def create_group_workload_controllerrs(self, group_name: str, **kwargs) -> TurboGroup:
        pass

    def update_group_workload_controllers(self, group_name: str, **kwargs) -> TurboGroup:
        pass
