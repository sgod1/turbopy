from turboapi.authenticator import Authenticator
from turboapi.turbo_api import TurboAPI

class GroupApiDTO:
    def __init__(self):
        pass

class ScheduleApiDTO:
    def __init__(self):
        pass

class TurboGroupApiDTO:
    def __init__(self, name: str):
        pass

class OnPremCostsManagerApiDTO:
    def __init__(self):
        pass

class RangeApiDTO:
    def __init__(self):
        pass

class SettingActivePolicyApiDTO:
    def __init__(self):
        pass

class SettingsApiDTOSerializable:
    def __init__(self):
        self.links = None
        self.uuid: str = str()
        self.displayName: str = str()
        self.className: str = str()
        self.value: str = str() # value of the setting
        self.valueType: str = str() # enum: [ STRING, NUMERIC, INTEGER, BOOLEAN, LIST, SECRET ]
        self.valueObjectType: str = str()
        self.entityType: str = str()
        self.range: RangeApiDTO = RangeApiDTO()
        self.activeSettingsPolicies: list[SettingActivePolicyApiDTO] = list()
        self.sourceGroupName: str = str()
        self.sourceGroupUuid: str = str()

class SettingsManagerApiDTO:
    def __init__(self):
        self.links = None
        self.settings = None
        self.uuid: str = str()
        self.displayName: str = str()
        self.className: str = str()
        self.entityType: str = str()
        self.category: str = str()
        self.settings: list[SettingsApiDTOSerializable] = list()

class SettingsPolicyApiDTO:
    def __init__(self):
        self.links = None
        self.uuid: str = str()
        self.displayName: str = str()
        self.className: str = str()
        self.entityType: str = str()
        self.scopes: list[GroupApiDTO] = list()
        self.settingsManagers: list[SettingsManagerApiDTO] = list()
        self.onPremCostManagers: list[OnPremCostsManagerApiDTO] = list()
        self.schedule: ScheduleApiDTO = ScheduleApiDTO()
        self.disabled: bool = False
        self.notes: str = str()
        self.readOnly: bool = False
        self.default: bool = False

class PolicSettingsyFactory(TurboAPI):
    def __init__(self, authenticator: Authenticator):
        super().__init__(authenticator)

    def create_workload_controller_policy(self, name: str, scope: str, **kwargs) -> bool:
        # check if policy exists

        # find workload controller scope (group)

        settings_policy = SettingsPolicyApiDTO()

        settings_policy.displayName = name
        settings_policy.scopes.append(GroupApiDTO()) # pass a list of scopes...
        settings_policy.entityType = "WorkloadController"

        settings_manager = SettingsManagerApiDTO()
        settings_manager.uuid = "automationmanager"
        settings_policy.settingsManagers.append(settings_manager)

        settiings_value = SettingsApiDTOSerializable()
        settiings_value.entityType = "WorkloadController"
        settings_manager.uuid="resizeCPULimitDown"
        settiings_value.value = kwargs["resize_cpu_limit_down"] # MANUAL
        settings_manager.settings.append(settiings_value)

        settiings_value = SettingsApiDTOSerializable()
        settiings_value.entityType = "WorkloadController"
        settings_manager.uuid="resizeMemLimitUp"
        settiings_value.value = kwargs["resize_mem_limit_up"] # MANUAL
        settings_manager.settings.append(settiings_value)

        # post to endpoint
        r = self.post('settingsPolicy', settings_policy)

        return True
