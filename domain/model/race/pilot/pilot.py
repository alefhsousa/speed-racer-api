from datetime import timedelta
from functools import reduce

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

    @property
    def race_duration(self):
        return reduce(lambda acc, lap: acc + lap.lap_time, self.laps, timedelta())

    @property
    def avg_speed(self):
        return round(reduce(lambda acc, lap: acc + lap.lap_speed, self.laps, 0) / self.total_laps, 2)
