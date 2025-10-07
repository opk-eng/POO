class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_dados(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

class Usuario:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Código: {self.codigo}")
#################################################################
from arquivo01 import Livro, Usuario

# Criar um objeto da classe Livro
livro1 = Livro("A Arte da Guerra", "Sun Tzu")

# Criar um objeto da classe Usuario
usuario1 = Usuario("João Silva", "U001")

# Usar os métodos exibir_dados() de cada objeto
print("Dados do Livro:")
livro1.exibir_dados()

print("\nDados do Usuário:")
usuario1.exibir_dados()
################################################################
class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontos = 0

    def adicionar_pontos(self, valor):
        self.pontos += valor

    def exibir_pontos(self):
        print(f"Jogador: {self.nome}, Pontos: {self.pontos}")
#################################################################
from arquivo01 import Jogador

# Criar um objeto da classe Jogador
jogador1 = Jogador("PlayerOne")

# Usar o método adicionar_pontos para adicionar pontos algumas vezes
jogador1.adicionar_pontos(10)
jogador1.adicionar_pontos(5)
jogador1.adicionar_pontos(20)

# Chamar o método exibir_pontos para mostrar o resultado final
jogador1.exibir_pontos()
