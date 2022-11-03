# cada classe deve ter uma única responsabilidade.
# entidades devem ser abertas para extensão, mas fechadas para modificação.
# CTRL + / para comentar as linhas

import datetime
import math


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, data_de_nascimento: datetime.date) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_de_nascimento = data_de_nascimento

    @property
    def idade(self) -> int:
        return math.floor((datetime.date.today() - self.data_de_nascimento).days / 365.2425)

    def __str__(self) -> str:
        return f"{self.nome} {self.sobrenome} tem {self.idade} anos."


class Curriculo:
    def __init__(self, pessoa: Pessoa, experiencias: list[str]) -> None:
        self.pessoa = pessoa
        self.experiencias = experiencias

    # Criando propriedades do curriculo
    @property
    def quantidade_de_experiencias(self) -> int:
        return len(self.experiencias)

    @property
    def empresa_atual(self) -> str:
        return self.experiencias[-1]
    # Criando método da experiência
    def adiciona_experiencia(self, experiencia: str) -> None:
        self.experiencias.append(experiencia)

    def __str__(self):
        return f"{self.pessoa.nome} {self.pessoa.sobrenome} tem {self.pessoa.idade} anos e já trabalhou " \
               f"em {self.quantidade_de_experiencias} empresas e atualmente trabalha na empresa {self.empresa_atual}."


hugo = Pessoa(nome='Hugo', sobrenome='Gusmão',
              data_de_nascimento=datetime.date(1986, 2, 17))

print(hugo)

curriculo_hugo = Curriculo(
    pessoa=hugo,
    experiencias=['Rede Ponto Certo', 'Elio Tecnologia', 'Cebrap', 'Freelancer', 'SPUrbanismo']
)

print(curriculo_hugo)
curriculo_hugo.adiciona_experiencia('Ministério das Cidades')
print(curriculo_hugo)


