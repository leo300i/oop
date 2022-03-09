class Material:

    def __init__(self, strength, flexibility, hardness, information):
        self.strength = strength
        self.flexibility = flexibility
        self.hardness = hardness
        self.information = information

    def information_material(self):
        print(self.information)


class Plastick(Material):

    def __init__(self, strength, flexibility, hardness, information):
        super().__init__(strength, flexibility, hardness, information)

    def information_material(self):
        print(f"{Plastick} бутылка")


class Glass(Material):

    def __init__(self, strength, flexibility, hardness, information):
        super().__init__(strength, flexibility, hardness, information)


class Iron(Material):

    def __init__(self, strength, flexibility, hardness, information):
        super().__init__(strength, flexibility, hardness, information)


class Wood(Material):

    def __init__(self, strength, flexibility, hardness, information):
        super().__init__(strength, flexibility, hardness, information)


class Rubber(Material):

    def __init__(self, strength, flexibility, hardness, information):
        super().__init__(strength, flexibility, hardness, information)


class Bottle(Plastick):

    def information_material(self):
        print(f'{Plastick} ')
