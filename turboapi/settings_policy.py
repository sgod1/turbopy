import json

class SettingsPolicyApiDTO:
    def __init__(self):
        self.displayName: str = str()
        self.entityType: str = str()
        self.settingsManagers: list[SettingsManagerApiDTO] = list()
        self.disabled = False
        self.note: str = str()
        self.readOnly = False
        self.default = False

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


class SettingsManagerApiDTO:
    def __init__(self):
        self.uuid: str|None = str()
        self.displayName: str|None = str()
        self.className: str|None = "string"
        self.category: str = str()
        self.settings: list[SettingApiDTOSerializable] = list()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


class SettingApiDTOSerializable:
    def __init__(self):
        self.uuid: str = str()
        self.displayName: str = str()
        self.defaultValue: str = str()
        self.categories = list()
        self.valueType: str = str()
        self.value: str = str()
        self.valueObjectType: str  = str()
        self.min: int = 0
        self.max: int = 0
        self.entityType: str = str()
        self.range: RangeApiDTO =RangeApiDTO()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)


class RangeApiDTO:
    def __init__(self):
        self.step: int = int(0)
        self.labels: list[str] = list()
        self.customStepValues: list[int] = list()
        self.stepValues: list[int] = list()

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=4)
