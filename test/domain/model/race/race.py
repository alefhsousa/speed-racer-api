from datetime import timedelta


class Race(object):

    def __init__(self, time, pilot_car, pilot_name, lap, lap_time, lap_speed):
        self.time = str(time)
        self.pilot_car = pilot_car
        self.pilot_name = pilot_name
        self.lap = lap
        self.lap_time = str(lap_time)
        self.lap_speed = str(lap_speed)

    @property
    def parsed_time(self):
        transform_str_to_float = lambda str: float(str)
        time_fields = list(map(transform_str_to_float, self.lap_time.replace(".", ":").split(":")))
        return timedelta(milliseconds=time_fields[2], seconds=time_fields[1], minutes=time_fields[0], hours=0)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
