from datetime import timedelta


def transform_str_to_float(item):
    return float(item)


class Lap(object):
    def __init__(self, number: int, lap_time: str, lap_speed):
        self.number = number
        self._lap_time = str(lap_time)
        self.lap_speed = lap_speed

    @property
    def lap_time(self) -> timedelta:
        time_fields = list(map(transform_str_to_float, self._lap_time.replace(".", ":").split(":")))
        return timedelta(milliseconds=time_fields[2], seconds=time_fields[1], minutes=time_fields[0], hours=0)
