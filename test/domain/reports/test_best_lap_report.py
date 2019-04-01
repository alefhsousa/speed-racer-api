from pytest import fixture

from domain.model.common.message import MessageCategory
from domain.reports.best_lap_report import BestLapReport
from test.domain.model.race.lap.lap_factory import LapFactory
from test.domain.model.race.pilot.pilot_factory import PilotFactory


class TestBestLapReport(object):

    @fixture
    def report(self):
        return BestLapReport()

    def test_should_return_a_valid_report(self, report):
        win_lap = LapFactory(number=2, lap_speed=30)
        best_laps = [win_lap, LapFactory(lap_speed=15)]
        other_pilot = PilotFactory(laps=[LapFactory(lap_speed=20)])
        another_pilot = PilotFactory(laps=[LapFactory(lap_speed=29)])

        pilot = PilotFactory(laps=best_laps)
        result = report.create_report([pilot, other_pilot, another_pilot])
        assert result.is_right
        report = result.value

        assert report['name'] == pilot.name
        assert report['lap'] == 2
        assert report['time'] == win_lap.lap_time

    def test_should_return_a_invalid_report_because_pilots_is_empty(self, report):
        result = report.create_report([])
        assert result.is_left

        message = result.value[0]

        assert message.category == MessageCategory.WARNING
        assert message.target == 'best_lap_report'
        assert message.key == 'without_pilots'
