import datetime


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento


hugo = Pessoa(nome='Hugo', sobrenome='Gusmão', data_de_nascimento=datetime.date(1986, 2, 17))

print(hugo)
print(hugo.nome)
print(hugo.sobrenome)
print(hugo.data_de_nascimento)
