from domain.model.common.message import Message, MessageCategory
from infrastructure.common.either import Either, Left, Right
from infrastructure.parser.log_validator import LogValidator


class RaceValidator(LogValidator):

    def validate(self, line_content, line_number) -> Either:
        violations = []

        try:
            str(line_content[0])
        except ValueError:
            violations.append(Message(category=MessageCategory.VALIDATION,
                                      key='invalid_time_format',
                                      args=(line_number, line_content['poc_id'])))

        try:
            car, pilot_name = str(line_content[1]).strip().split('–')
            try:
                int(car)
            except ValueError:
                violations.append(Message(category=MessageCategory.VALIDATION,
                                          key='invalid_car_number',
                                          args=(line_number, line_content[1])))

            if not pilot_name:
                violations.append(Message(category=MessageCategory.VALIDATION,
                                          key='invalid_pilot_name',
                                          args=(line_number, line_content[1])))
        except ValueError:
            violations.append(Message(category=MessageCategory.VALIDATION,
                                      key='invalid_pilot_name',
                                      args=(line_number, line_content[1])))

        try:
            int(line_content[2])
        except ValueError:
            violations.append(Message(category=MessageCategory.VALIDATION,
                                      key='invalid_lap_times',
                                      args=(line_number, line_content[2])))

        try:
            float(line_content[4].replace(',', '.'))
        except ValueError:
            violations.append(Message(category=MessageCategory.VALIDATION,
                                      key='invalid_lap_speed',
                                      args=(line_number, line_content[4])))

        if violations:
            return Left(violations)

        return Right(None)
