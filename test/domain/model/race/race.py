class Race(object):

    def __init__(self, time, pilot_car, pilot_name, lap, lap_time, lap_speed):
        self.time = str(time)
        self.pilot_car = pilot_car
        self.pilot_name = pilot_name
        self.lap = lap
        self.lap_time = str(lap_time)
        self.lap_speed = str(lap_speed)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
