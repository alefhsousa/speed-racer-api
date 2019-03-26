import os

from pytest import fixture

from infrastructure import Configuration


class TestConfiguration:

    @fixture
    def config(self):
        return Configuration()

    def test_should_return_value_from_config_file(self, config):
        assert config
        assert config.name
        assert 'speed-racer' == config.name

    def test_should_return_value_from_environment_variable(self, config):
        os.environ['name'] = 'root'
        assert config
        assert config.name
        assert 'root' == config.name
