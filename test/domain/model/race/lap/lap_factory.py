import factory
from factory import BUILD_STRATEGY, lazy_attribute, Sequence
from faker import Faker

from domain.model.race.lap.lap import Lap

fake = Faker()


class LapFactory(factory.Factory):
    class Meta:
        strategy = BUILD_STRATEGY
        model = Lap

    number = Sequence(lambda n: n + 1)
    lap_time = lazy_attribute(lambda o: fake.time_object())
    lap_speed = lazy_attribute(lambda o: float(fake.random_number()))

