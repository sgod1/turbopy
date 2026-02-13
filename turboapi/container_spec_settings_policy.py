from turboapi.settings_policy import SettingsPolicyApiDTO, SettingsManagerApiDTO, SettingApiDTOSerializable, RangeApiDTO


def container_spec_settings_policy(**kwargs) -> SettingsPolicyApiDTO:

    policy_dto = SettingsPolicyApiDTO()

    policy_dto.displayName = kwargs["displayName"]
    policy_dto.entityType = "ContainerSpec"

    policy_dto.note = "note 1"

    settings_manager_dto = SettingsManagerApiDTO()
    policy_dto.settingsManagers.append(settings_manager_dto)

    settings_manager_dto.uuid = "marketsettingsmanager"
    settings_manager_dto.displayName = "Operational Constraints"
    settings_manager_dto.category = "Analysis"

    # min observation period setting
    min_observation_period = SettingApiDTOSerializable()
    settings_manager_dto.settings.append(min_observation_period)

    min_observation_period.uuid = "minObservationPeriodContainerSpec"
    min_observation_period.displayName = "Min Observation Period"
    min_observation_period.value = "1.0"
    min_observation_period.defaultValue = "1.0"
    min_observation_period.categories = ["resizeRecommendationsConstants"]
    min_observation_period.valueType = "NUMERIC"
    min_observation_period.valueObjectType = "String"
    min_observation_period.min = 0
    min_observation_period.max = 90
    min_observation_period.entityType = "ContainerSpec"

    set_range = False

    if set_range:
        value_range = min_observation_period.range

        value_range.step = 1
        value_range.labels = ["More Elastic","","","Less Elastic","None","1 day","3 days","7 days"]
        value_range.customStepValues = [0,1,3,7]
        value_range.stepValues = [0,1,3,7]

    else:
        delattr(min_observation_period, "range")

    return policy_dto

if __name__ == "__main__":
    policy_dto = container_spec_settings_policy(displayName="api-policy-container-spec-1")

    print(policy_dto.to_json())
