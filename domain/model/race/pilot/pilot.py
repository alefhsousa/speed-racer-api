from domain.model.race.lap.lap import Lap


class Pilot(object):

    def __init__(self, number: str, name: str, laps: [Lap]):
        self.number = number
        self.name = name
        self.laps = laps

    @property
    def total_laps(self) -> int:
        return len(self.laps)

    @property
    def finished(self) -> bool:
        return self.total_laps == 4
