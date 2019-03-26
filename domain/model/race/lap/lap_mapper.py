from domain.model.race.lap.lap import Lap


class LapMapper(object):

    def to_model(self, line_content) -> Lap:
        return Lap(number=int(line_content[2]), lap_time=line_content[3].strip(),
                   lap_speed=float(line_content[4].replace(',', '.').strip()))

    def to_models(self, lines_content) -> list:
        return list(map(self.to_model, lines_content))
