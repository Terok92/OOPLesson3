from Cars import Car


class Ferrari(Car):
    def __init__(self, speed, color, types, convertible):
        Car.__init__(self, speed)
        self.color = color
        self.type = types
        self.convertible = convertible

    def is_speed_exceeded(self):
        if self.max_speed() < self.speed:
            return "Yes"
        else:
            return "No"

    def get_color(self):
        return f"My color is {self.color}."

    def get_type(self):
        return f"My type is {self.type}."

    def get_convertible(self):
        return f"Am I convertible? {self.convertible}."