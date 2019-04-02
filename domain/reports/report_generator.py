from abc import ABC, abstractmethod

from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot import Pilot
from domain.reports.average_time_report import AverageTimeReport
from domain.reports.best_lap_pilot_report import BestLapPilotReport
from domain.reports.best_lap_report import BestLapReport
from domain.reports.default_report import DefaultReport
from domain.reports.time_after_winner_report import TimeAfterWinnerReport
from infrastructure.common.either import Either, Left, Right
from infrastructure.parser.log_parser import LogParser


class ReportGenerator(object):

    def __init__(self):
        default_report = DefaultReport()
        average_time_report = AverageTimeReport()
        best_lap_pilot_report = BestLapPilotReport()
        best_lap_pilot = BestLapReport()
        time_after_winner_report = TimeAfterWinnerReport()
        self.reports = {
            default_report.name: default_report,
            average_time_report.name: average_time_report,
            best_lap_pilot_report.name: best_lap_pilot_report,
            best_lap_pilot.name: best_lap_pilot,
            time_after_winner_report.name: time_after_winner_report
        }

    def process_report(self, name: str) -> Either:

        try:
            report_to_process = self.reports[name]
            result = LogParser().process_log().value
            return report_to_process.create_report(result)
        except KeyError:
            valid_report_names = list(map(lambda report_name: str(report_name), self.reports.keys()))
            return Left([Message(category=MessageCategory.VALIDATION, key='invalid_report_name',
                                 args=(name, valid_report_names))])
