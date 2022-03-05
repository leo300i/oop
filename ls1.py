class Car:
    currentSpeed = 0

    def __init__(self, title, model, colour, max_speed, speed):
        # print(title, model, colour)
        self.title = title
        self.model = model
        self.color = colour
        self.max_speed = max_speed
        self.speed = speed

    def start_engine(self):
        print(f"on {self.title} {self.model} engine started!")

    def gas(self):
        if self._currentSpeed >= self.max_speed:
            print('check on')
        else:
            self._currentSpeed += self.speed
            print(self._currentSpeed)


"""Instance"""

bmw = Car('BMW', 'E38', 'bLUE', 360, 20)
bmw.start_engine()

mercedes = Car('mercedes', 'w220', 'black', 360, 10)
mercedes.start_engine()
