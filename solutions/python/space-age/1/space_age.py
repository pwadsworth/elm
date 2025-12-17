import inspect

SECS_YR = 365.25 * 24 * 3600
PERIOD = { "mercury": 0.2408467,
            "venus": 0.61519726,
            "earth": 1.0,
            "mars": 1.8808158,
            "jupiter": 11.862615,
            "saturn": 29.447498,
            "uranus": 84.016846,
            "neptune": 164.79132 }

class SpaceAge:
 
    def __init__(self, seconds):
        self.seconds = seconds
    def on_mercury(self):
        return calculate_this_planet(self)
    def on_venus(self):
        return calculate_this_planet(self)
    def on_earth(self):
        return calculate_this_planet(self)
    def on_mars(self):
        return calculate_this_planet(self)
    def on_jupiter(self):
        return calculate_this_planet(self)
    def on_saturn(self):
        return calculate_this_planet(self)
    def on_uranus(self):
        return calculate_this_planet(self)
    def on_neptune(self):
        return calculate_this_planet(self)

def calculate_this_planet(self):
    return round(self.seconds / (SECS_YR * PERIOD[inspect.stack()[1].function[3:]]), 2)    