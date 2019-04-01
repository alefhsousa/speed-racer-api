import factory
from factory import BUILD_STRATEGY, lazy_attribute, Sequence
from faker import Faker

from domain.model.race.pilot.pilot import Pilot
from test.domain.model.race.lap.lap_factory import LapFactory

fake = Faker()


class PilotFactory(factory.Factory):
    class Meta:
        strategy = BUILD_STRATEGY
        model = Pilot

    number = Sequence(lambda n: n + 1)
    name = lazy_attribute(lambda o: fake.name())
    laps = LapFactory.generate_batch(BUILD_STRATEGY, 2)
