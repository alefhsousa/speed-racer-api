from factory import BUILD_STRATEGY
from pytest import fixture

from domain.model.common.message import MessageCategory
from domain.reports.default_report import DefaultReport
from domain.reports.time_after_winner_report import TimeAfterWinnerReport
from test.domain.model.race.lap.lap_factory import LapFactory
from test.domain.model.race.pilot.pilot_factory import PilotFactory


class TestDefaultReport(object):

    @fixture
    def report(self):
        return TimeAfterWinnerReport()

    def test_should_return_a_valid_report(self, report):
        winner_laps = LapFactory.generate_batch(BUILD_STRATEGY, 4, lap_time='1:01.0')
        loser_laps = LapFactory.generate_batch(BUILD_STRATEGY, 4, lap_time='1:03.0')

        winner_pilot = PilotFactory(laps=winner_laps)
        loser_pilot = PilotFactory(laps=loser_laps)
        incomplete_race = PilotFactory(laps=[])

        result = report.create_report([winner_pilot, loser_pilot, incomplete_race])
        assert result.is_right
        report = result.value

        assert len(report) == 2

        assert report[0]['position'] == 1
        assert report[0]['pilot_number'] == winner_pilot.number
        assert report[0]['name'] == winner_pilot.name
        assert report[0]['total_laps'] == winner_pilot.total_laps
        assert report[0]['total_time'] == winner_pilot.race_duration

        assert report[1]['position'] == 2
        assert report[1]['pilot_number'] == loser_pilot.number
        assert report[1]['name'] == loser_pilot.name
        assert report[1]['total_laps'] == loser_pilot.total_laps
        assert report[1]['total_time'] == loser_pilot.race_duration
        assert report[1]['time_after_winner'].seconds == 8

    def test_should_return_a_invalid_report_because_none_pilots_completed_laps(self, report):
        winner_laps = LapFactory.generate_batch(BUILD_STRATEGY, 2, lap_time='1:01.0')
        loser_laps = LapFactory.generate_batch(BUILD_STRATEGY, 3, lap_time='1:03.0')

        winner_pilot = PilotFactory(laps=winner_laps)
        loser_pilot = PilotFactory(laps=loser_laps)
        incomplete_race = PilotFactory(laps=[])

        result = report.create_report([winner_pilot, loser_pilot, incomplete_race])
        assert result.is_left

        message = result.value[0]

        assert message.category == MessageCategory.WARNING
        assert message.target == 'timer_after_winner'
        assert message.key == 'without_winner_pilots'

    def test_should_return_a_invalid_report_because_pilots_is_empty(self, report):

        result = report.create_report([])
        assert result.is_left

        message = result.value[0]

        assert message.category == MessageCategory.WARNING
        assert message.target == 'timer_after_winner'
        assert message.key == 'without_pilots'

