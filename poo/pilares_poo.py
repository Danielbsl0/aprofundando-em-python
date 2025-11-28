#Herança
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    def emitir_som(self):
        pass
    
class Cachorro(Animal): #Filho
    def emitir_som(self): #Mesmo método mas com comportamento diferente -> Polimorfismo
        return "Au, Au"
    
class Gato(Animal):
      def emitir_som(self):
        return "Miau!"
      
dog = Cachorro("Rex")
cat = Gato("Felix")

print("Exemplo de Polimorfismo")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz {animal.emitir_som()}")

print("Encapsulamento: ")

class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo #Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    
conta = ContaBancaria(1000)
print(f"Saldo da conta bancaria: {conta.consultar_saldo()}")
conta.depositar(500)
conta.depositar(-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")


#Abstração
print("\nExemplo de abstração")
from abc import ABC, abstractmethod

class Veiculo(ABC): #Definir um molde para a classe
    
    @abstractmethod #Decorador que explícita uma classe abstrata (obrigatoriedade)
    def ligar(self):
        pass
    
    def desligar(self):
        pass
    
class Carro(Veiculo):
    def __init__(self):
        super().__init__()

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"
    
carro_amarelo = Carro()
print(carro_amarelo.ligar())
print(carro_amarelo.desligar())
