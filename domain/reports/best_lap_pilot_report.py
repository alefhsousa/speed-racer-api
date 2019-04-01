from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.report import Report
from infrastructure.common.either import Either, Right, Left


class BestLapPilotReport(Report):

    @property
    def name(self):
        return 'best_lap_pilot'

    def create_report(self, pilots: [Pilot]) -> Either:
        report = list()
        if pilots:
            for pilot in pilots:
                summary = dict()
                best_lap = max(pilot.laps, key=lambda lap: lap.lap_speed)
                summary['name'] = pilot.name
                summary['lap'] = best_lap.number
                summary['time'] = best_lap.lap_time

                report.append(summary)

            return Right(report)
        else:
            return Left([Message(category=MessageCategory.WARNING, target='best_lap_pilot_report', key='without_pilots')])
