import random
import string

import factory
from factory import BUILD_STRATEGY, lazy_attribute
from faker import Faker

from test.domain.model.race.race import Race

fake = Faker()
years18_in_days = '-6750d'


class RaceFactory(factory.Factory):
    class Meta:
        strategy = BUILD_STRATEGY
        model = Race

    time = lazy_attribute(lambda o: fake.time_object())
    pilot_car = lazy_attribute(lambda o: int(''.join(random.choice(string.digits) for _ in range(4))))
    pilot_name = lazy_attribute(lambda o: fake.name())
    lap = lazy_attribute(lambda o: random.randint(1, 4))
    lap_time = lazy_attribute(lambda o: fake.time_object())
    lap_speed = lazy_attribute(lambda o: float(fake.random_number()))

    @staticmethod
    def to_input(race=None):
        race = race or RaceFactory()
        return tuple([str(race.time), str(race.pilot_car) + ' – ' + race.pilot_name, race.lap, str(race.lap_time),
                      str(race.lap_speed).replace('.', ',')])
