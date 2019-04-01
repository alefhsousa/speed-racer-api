from pytest import fixture

from domain.model.common.message import MessageCategory
from domain.reports.average_time_report import AverageTimeReport
from test.domain.model.race.lap.lap_factory import LapFactory
from test.domain.model.race.pilot.pilot_factory import PilotFactory


class TestAverageTimeReport(object):

    @fixture
    def report(self):
        return AverageTimeReport()

    def test_should_return_a_valid_report(self, report):
        best_laps = [LapFactory(number=2, lap_speed=30), LapFactory(lap_speed=15)]
        other_pilot = PilotFactory(laps=[LapFactory(number=1, lap_speed=20), LapFactory(lap_speed=10)])
        another_pilot = PilotFactory(laps=[LapFactory(number=4, lap_speed=29), LapFactory(number=6, lap_speed=19)])
        pilot = PilotFactory(laps=best_laps)
        result = report.create_report([pilot, other_pilot, another_pilot])
        assert result.is_right
        report = result.value

        report_pilot_report = list(filter(lambda r: r['name'] == pilot.name, report))
        another_pilot_report = list(filter(lambda r: r['name'] == another_pilot.name, report))
        other_pilot_report = list(filter(lambda r: r['name'] == other_pilot.name, report))

        assert report_pilot_report[0]['name'] == pilot.name
        assert report_pilot_report[0]['averageSpeed'] == 22.50

        assert another_pilot_report[0]['name'] == another_pilot.name
        assert another_pilot_report[0]['averageSpeed'] == 24.00

        assert other_pilot_report[0]['name'] == other_pilot.name
        assert other_pilot_report[0]['averageSpeed'] == 15.00

    def test_should_return_a_invalid_report_because_pilots_is_empty(self, report):
        result = report.create_report([])
        assert result.is_left

        message = result.value[0]

        assert message.category == MessageCategory.WARNING
        assert message.target == 'average_time_report'
        assert message.key == 'without_pilots'
