# import requisites
import datetime
import math


# create class
class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} {self.idade} anos."


hugo = Pessoa(nome='Hugo', sobrenome='Gusmão',
              data_de_nascimento=datetime.date(1986, 2, 17))

print(hugo)
print(hugo.nome)
print(hugo.sobrenome)
print(hugo.data_de_nascimento)

print(hugo.idade)

