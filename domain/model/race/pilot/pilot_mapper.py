from domain.model.race.lap.lap_mapper import LapMapper
from domain.model.race.pilot.pilot import Pilot
from infrastructure.parser.log_mapper import LogMapper


class PilotMapper(LogMapper):

    def __init__(self, lap_mapper=None):
        self.lap_mapper = lap_mapper or LapMapper()

    def to_model(self, line_content) -> Pilot:
        laps = self.lap_mapper.to_models(line_content[1])
        car, pilot_name = str(line_content[1][0][1]).strip().split('–')
        return Pilot(number=str(car).strip(), name=str(pilot_name).strip(), laps=laps)

    def to_models(self, lines_content) -> [Pilot]:
        return list(map(lambda item: self.to_model(item), lines_content.items()))
