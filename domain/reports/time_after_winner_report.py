from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.report import Report
from infrastructure.common.either import Right, Left


class TimeAfterWinnerReport(Report):

    @property
    def name(self):
        return 'timer_after_winner'

    def create_report(self, pilots: [Pilot]):

        if not pilots:
            return Left(
                [Message(category=MessageCategory.WARNING, target='timer_after_winner', key='without_pilots')])

        report = []
        winner_pilots = list(filter(lambda pilot: pilot.finished, pilots))
        winner_pilots.sort(key=lambda pilot: pilot.race_duration)

        if winner_pilots:
            winner = winner_pilots[0]
            for index, pilot in enumerate(winner_pilots):
                summary = dict()
                summary['position'] = index + 1
                summary['pilot_number'] = pilot.number
                summary['name'] = pilot.name
                summary['total_laps'] = pilot.total_laps
                summary['total_time'] = pilot.race_duration
                if index + 1 > 1:
                    summary['time_after_winner'] = pilot.race_duration - winner.race_duration
                report.append(summary)

            return Right(report)
        else:
            return Left([Message(category=MessageCategory.WARNING, target='timer_after_winner',
                                 key='without_winner_pilots')])
