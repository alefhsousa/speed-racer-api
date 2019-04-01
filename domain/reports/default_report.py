from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.report import Report
from infrastructure.common.either import Right, Left


class DefaultReport(Report):

    @property
    def name(self):
        return 'default'

    def create_report(self, pilots: [Pilot]):
        report = []
        winner_pilots = list(filter(lambda pilot: pilot.finished, pilots))
        winner_pilots.sort(key=lambda pilot: pilot.race_duration)

        if winner_pilots:
            for index, pilot in enumerate(winner_pilots):
                summary = dict()
                summary['position'] = index + 1
                summary['pilot_number'] = pilot.number
                summary['name'] = pilot.name
                summary['total_laps'] = pilot.total_laps
                summary['total_time'] = pilot.race_duration
                report.append(summary)

            return Right(report)
        else:
            return Left([Message(category=MessageCategory.WARNING, target='default_report', key='without_winner_pilots')])
