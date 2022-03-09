class Animal:

    def __init__(self, name, type, color, voicetxt):
        self.name = name
        self.type = type
        self.color = color
        self.voicetxt = voicetxt

    def voice(self):
        print(self.voicetxt)


""""наследование"""


class Dog(Animal):

    def __init__(self, name, type, color, voicetxt):
        super().__init__(name, type, color, voicetxt)


class Cat(Animal):

    def __init__(self, name, type, color, voicetxt):
        super().__init__(name, type, color, voicetxt)


rex = Dog('rex', 'domestics', 'blue', 'gafgaf')
rex.voice()

barsik = Cat('Barsik', 'dometics', '_', 'maymay')
barsik.voice()

""""полиформиз"""


class Horse(Animal):

    def __init__(self, name, type, color, voicetxt, speed, weight):
        super().__init__(name, type, color, voicetxt)
        self.speed = speed
        self.weight = weight

    def voice(self):
        print(f"{self.name}: {self.voicetxt}")


mustang = Horse("mustang", ' domestic', 'brown', 'frrrr', 30, 250)
mustang.voice()


""""инкапсуляция"""
