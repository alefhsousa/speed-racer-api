from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.report import Report
from infrastructure.common.either import Either, Right, Left


class AverageTimeReport(Report):

    @property
    def name(self):
        return 'average_time_report'

    def create_report(self, pilots: [Pilot]) -> Either:
        report = list()
        if pilots:
            for pilot in pilots:
                summary = dict()
                summary['name'] = pilot.name
                summary['number'] = pilot.number
                summary['averageSpeed'] = pilot.avg_speed

                report.append(summary)

            return Right(report)
        else:
            return Left([Message(category=MessageCategory.WARNING, target='average_time_report', key='without_pilots')])
