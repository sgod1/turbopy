from enum import StrEnum

from turboapi.authenticator import Authenticator
from turboapi.turbo_api import TurboAPI

class ActionModes(StrEnum):
    DISABLED = "DISABLED"
    RECOMMEND = "RECOMMEND"
    EXTERNAL_APPROVAL = "EXTERNAL_APPROVAL"
    MANUAL = "MANUAL"
    AUTOMATIC = "AUTOMATIC"
    EXTERNAL = "EXTERNAL"


class TurboAction:
    def __init__(self) -> None:
        pass

        #{'uuid': '638810435460873', 'displayName': 'RECOMMEND', 'actionImpactID': 638810435460873,
        # 'marketID': 777777, 'createTime': '2025-04-04T05:58:46Z', 'actionType': 'SUSPEND', 'actionState': 'READY',
        # 'actionMode': 'RECOMMEND',
        # 'details': 'Suspend Container Pod openshift-machine-config-operator/kube-rbac-proxy-crio-worker27.roky.szesto.io',
        # 'importance': -1.0,
        # 'target': {'uuid': '75860481769689', 'displayName': 'openshift-machine-config-operator/kube-rbac-proxy-crio-worker27.roky.szesto.io',
        # 'className': 'ContainerPod', 'environmentType': 'HYBRID',
        # 'discoveredBy': {'uuid': '75860481181760', 'displayName': 'Kubernetes-roky', 'isProbeRegistered': False,
        # 'type': 'Kubernetes', 'readonly': False}, 'vendorIds': {'Kubernetes-roky': 'f1cc6f83-4635-43c0-bf3c-e3d32ea3e014'},
        # 'state': 'ACTIVE', 'aspects': {'containerPlatformContextAspect': {'namespace': 'openshift-machine-config-operator',
        # 'containerPlatformCluster': 'Kubernetes-roky', 'namespaceEntity': {'uuid': '75860481770018',
        # 'displayName': 'openshift-machine-config-operator', 'className': 'Namespace'},
        # 'containerClusterEntity': {'uuid': '75860481771214', 'displayName': 'Kubernetes-roky', 'className': 'ContainerPlatformCluster'},
        # 'type': 'ContainerPlatformContextAspectApiDTO'}},
        # 'tags': {'[k8s toleration] NoSchedule': ['node.kubernetes.io/memory-pressure Exists'], '[k8s toleration] NoExecute': ['Exists'],
        # 'IsVirtualMachineInstance': ['false']}}, 'currentEntity': {'uuid': '75860481769689',
        # 'displayName': 'openshift-machine-config-operator/kube-rbac-proxy-crio-worker27.roky.szesto.io', 'className': 'ContainerPod', 'environmentType': 'HYBRID',
        # 'discoveredBy': {'uuid': '75860481181760', 'displayName': 'Kubernetes-roky', 'isProbeRegistered': False, 'type': 'Kubernetes', 'readonly': False},
        # 'vendorIds': {'Kubernetes-roky': 'f1cc6f83-4635-43c0-bf3c-e3d32ea3e014'}, 'state': 'ACTIVE',
        # 'tags': {'[k8s toleration] NoSchedule': ['node.kubernetes.io/memory-pressure Exists'], '[k8s toleration] NoExecute': ['Exists'],
        # 'IsVirtualMachineInstance': ['false']}}, 'risk': {'subCategory': 'Efficiency Improvement',
        # 'description': 'Suspend openshift-machine-config-operator/kube-rbac-proxy-crio-worker27.roky.szesto.io on suspended worker27.roky.szesto.io',
        # 'severity': 'MINOR', 'importance': 0.0}, 'source': 'MARKET', 'relatedActionsCountByType': {'CAUSED_BY': 1},
        # 'actionID': 638810435460873}

class ActionFactory(TurboAPI):
    def __init__(self, authenticator: Authenticator) -> None:
        super().__init__(authenticator)

    def list_actions(self) -> None:
        pass
