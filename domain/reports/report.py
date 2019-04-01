from abc import ABC, abstractmethod

from domain.model.race.pilot.pilot import Pilot
from infrastructure.common.either import Either


class Report(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def create_report(self, pilots: [Pilot]) -> Either:
        pass
