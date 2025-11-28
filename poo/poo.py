class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá meu nome é {self.nome} e eu tenho {self.idade} anos."
  
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print(mensagem)