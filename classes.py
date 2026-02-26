from personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida= 25, ataque= 3)

        
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida= 15, ataque= 4)


def criar_personagem():
         nome = input("nome do personagem: ")


         print("Selecione a opção para escolher a classe: \n 1 para guerreiro \n 2 para mago")
         escolha = input("Numero selecionado é?")

         if escolha == "1":
            jogador = Guerreiro(nome)
         elif escolha == "2":
            jogador = Mago(nome)
         else: 
            jogador = Guerreiro(nome)
            print("Opção invalida, por padrão sera guerreiro!")


         return jogador
        