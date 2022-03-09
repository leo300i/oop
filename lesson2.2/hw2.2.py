class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Jack(Person):
    _n = 99

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


class Vito(Jack):

    def __init__(self, first_name, last_name, phone_number, balance):
        super().__init__(first_name, last_name, phone_number, balance)

    def minus(self, jack_):
        o = jack_.balance - self._n
        f = o + self.balance
        print(f)


g = Jack('df', 'ff','fff', 100)
d = Vito('dd', 'dd', '22', 10)

Vito.minus(d, g)