import datetime
import math


class LivingBeing:
    def __init__(self, name: str, date_of_birth: datetime.date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        return math.floor((datetime.date.today() - self.date_of_birth).days / 365.2425)

    def make_noise(self, noise: str):
        print(f'{self.name} falou: {noise}')


class PeopleHeritage(LivingBeing):
    def __str__(self) -> str:
        return f'{self.name} tem {self.age} anos.'

    def speak(self, text):
        return self.make_noise(text)


class Dog(LivingBeing):
    def __init__(self, name: str, date_of_birth: datetime.date, breed):
        self.breed = breed
        super().__init__(name, date_of_birth)

    def __str__(self):
        return f'{self.name} é da raça {self.breed} e tem {self.age} anos.'

    def barf(self):
        return self.make_noise('Au Au!')


cachorro = Dog(name='Kalinda', date_of_birth=datetime.date(2014, 2, 10), breed='Vira-Lata')
print(cachorro)
cachorro.barf()

pessoa = LivingBeing(name='Hugo', date_of_birth=datetime.date(1986, 2, 17))
print(pessoa.name)
print(pessoa.date_of_birth)
print(pessoa.age)

cachorro.barf()
pessoa.make_noise(f'Fica quieta {cachorro.name}!')
