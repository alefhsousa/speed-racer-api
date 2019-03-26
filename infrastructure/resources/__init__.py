from os import path

RESOURCES_DIR = path.dirname(path.abspath(__file__))
CONFIGURATION_FILE = path.join(RESOURCES_DIR, 'configuration.yml')
SPEED_RACER_FILE = path.join(RESOURCES_DIR, 'speedracer.data')

assert path.exists(CONFIGURATION_FILE), f'File {CONFIGURATION_FILE} not found.'
assert path.exists(SPEED_RACER_FILE), f'File {SPEED_RACER_FILE} not found.'
