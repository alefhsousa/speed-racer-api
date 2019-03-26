from collections import defaultdict

from pytest import fixture

from domain.model.race.pilot.pilot_mapper import PilotMapper
from test.domain.model.race.race_input_factory import RaceFactory


class TestPilotMapper(object):

    @fixture
    def mapper(self):
        return PilotMapper()

    def test_should_return_a_race_instance(self, mapper):
        fake_input = RaceFactory()
        grouped_data = defaultdict(list)
        grouped_data[fake_input.pilot_car] = [RaceFactory.to_input(fake_input)]
        returned_pilot = mapper.to_models(grouped_data)[0]
        assert not returned_pilot.finished
        assert returned_pilot.total_laps == 1
        assert returned_pilot.name == fake_input.pilot_name
