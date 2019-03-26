from pytest import fixture

from domain.model.race.race_validator import RaceValidator
from test.domain.model.race.race_input_factory import RaceFactory


class TestRaceValidator(object):

    @fixture
    def validator(self):
        return RaceValidator()

    def test_default_fixture_should_be_valid(self, validator):
        race = RaceFactory.to_input()
        result = validator.validate(race, 0)
        assert result.is_right
        assert not result.is_left

    def test_pilot_car_should_be_valid(self, validator):
        race = RaceFactory.to_input(RaceFactory(pilot_car='test'))
        result = validator.validate(race, 0)
        assert not result.is_right
        assert result.is_left
        assert result.value[0].key == 'invalid_car_number'

    def test_pilot_name_should_be_valid(self, validator):
        race = RaceFactory.to_input(RaceFactory(pilot_name=''))
        result = validator.validate(race, 0)
        assert not result.is_right
        assert result.is_left
        assert result.value[0].key == 'invalid_pilot_name'

    def test_lap_should_be_valid(self, validator):
        race = RaceFactory.to_input(RaceFactory(lap='a'))
        result = validator.validate(race, 0)
        assert not result.is_right
        assert result.is_left
        assert result.value[0].key == 'invalid_lap_times'

    def test_lap_speed_should_be_valid(self, validator):
        race = RaceFactory.to_input(RaceFactory(lap_speed='32:32'))
        result = validator.validate(race, 0)
        assert not result.is_right
        assert result.is_left
        assert result.value[0].key == 'invalid_lap_speed'

