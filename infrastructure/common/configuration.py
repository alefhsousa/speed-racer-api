import os
from collections import UserDict

import yaml

from infrastructure.common.environment import Environment
from infrastructure.resources import CONFIGURATION_FILE


class Configuration(UserDict):
    def __init__(self):
        super().__init__()
        self._environment = os.environ.get('ENVIRONMENT', Environment.TEST.name)
        with open(CONFIGURATION_FILE, 'r') as file:
            data = yaml.safe_load(file)

        self.data = data

    @property
    def environment(self) -> str:
        return self._environment

    @property
    def name(self) -> str:
        return self.get_key('name')

    def get_key(self, key):
        env_value = os.environ.get(key)
        if env_value:
            return env_value
        else:
            return self.data[self.environment][key]
