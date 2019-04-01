from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.report import Report
from infrastructure.common.either import Either, Right, Left


class BestLapReport(Report):

    @property
    def name(self):
        return 'best_lap'

    def create_report(self, pilots: [Pilot]) -> Either:
        if pilots:
            summary = dict()
            best_lap = None
            best_lap_speed = 0
            best_pilot = None
            for pilot in pilots:
                temp_best_lap = max(pilot.laps, key=lambda lap: lap.lap_speed)
                if temp_best_lap.lap_speed > best_lap_speed:
                    best_lap = temp_best_lap
                    best_pilot = pilot
                    best_lap_speed = temp_best_lap.lap_speed

            if best_lap:
                summary['name'] = best_pilot.name
                summary['lap'] = best_lap.number
                summary['time'] = best_lap.lap_time
                return Right(summary)
        else:
            return Left([Message(category=MessageCategory.WARNING, target='best_lap_report', key='without_pilots')])
