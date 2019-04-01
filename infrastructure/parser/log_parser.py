import re
from collections import defaultdict

from domain.model.common.message import Message, MessageCategory
from domain.model.race.pilot.pilot_mapper import PilotMapper
from domain.model.race.race_validator import RaceValidator
from infrastructure.common.either import Left, Right, Either
from infrastructure.resources import SPEED_RACER_FILE


class LogParser(object):

    def __init__(self):
        self.time_pattern = '\d{2}\:\d{2}\:\d{2}\.\d{3}'
        self.car_pilot_pattern = '\d{3}\s.\s\w*\.*\w*'
        self.lap_pattern = '\d+'
        self.lap_time_pattern = '\d+\:\d{2}\.\d{3}'
        self.avg_speed_pattern = '\d+\,*\d*'
        self.separator = '\s{2,}'
        self.validator = RaceValidator()
        self.mapper = PilotMapper()

    def _pattern_agregattor(self, data):
        index, value = data
        if index == 4:
            return '({})'.format(value)

        return '({})'.format(value + self.separator)

    def _make_regex(self):
        all_patterns = [self.time_pattern, self.car_pilot_pattern, self.lap_pattern, self.lap_time_pattern, self.avg_speed_pattern]
        groups = list(map(self._pattern_agregattor, enumerate(all_patterns)))
        return ''.join(groups)

    def _extract_pilot_number_from_tuple(self, tuple_data) -> str:
        return tuple_data[1].strip().split('–')[0].strip()

    def process_log(self) -> Either:
        violations = []
        grouped_data = defaultdict(list)
        with open(SPEED_RACER_FILE, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if len(lines) <= 1:
                return Left([Message(MessageCategory.VALIDATION, target='log-file', key='invalid_log')])

            line_pattern_extractor = re.compile(self._make_regex())

            for index, line in enumerate(lines[1:]):
                data = re.search(line_pattern_extractor, line)
                result = self.validator.validate(data.groups(), index)

                if result.is_right:
                    tuple_data = data.groups()
                    tuple_data[1].strip().split('–')[0].strip()
                    key = self._extract_pilot_number_from_tuple(tuple_data)
                    if key:
                        grouped_data[key].append(tuple_data)
                else:
                    violations += [violation for violation in result.value]

        if violations:
            return Left(violations)

        return Right(self.mapper.to_models(grouped_data))
