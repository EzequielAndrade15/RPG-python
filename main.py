# main.py
from personagem import Personagem
from inimigo import Inimigo
from batalha import batalha
from salvar import salvar_personagem, carregar_personagem
from classes import Guerreiro, Mago, criar_personagem
from produto import Pocao

def loja(jogador):
    print("\n=== Loja ===")
    pocao = Pocao("Poção de Vida", 50, "Recupera 20 de vida", bonus_vida=20, bonus_ataque=0)
    print(f"1 - {pocao.nome} | Preço: {pocao.preco} | {pocao.descricao}")

    escolha = input("Deseja comprar esta poção? (s/n) ")
    if escolha.lower() == "s":
        if not hasattr(jogador, "pocoes"):
            jogador.pocoes = []
        jogador.pocoes.append(pocao)
        print(f"{pocao.nome} comprada! Você agora tem {len(jogador.pocoes)} poção(ões).")
    else:
        print("Não comprou nada.")
    print("Saindo da loja...\n")

def main():
    print("=== Bem-vindo ao RPG ===")
    jogador = criar_personagem()

    # Criar inimigos
    goblin = Inimigo("Goblin", 15, 2, 15)
    esqueleto = Inimigo("Esqueleto", 12 , 3, 17)

    while True:
        print("\n=== Menu ===")
        menu = input("Digite 1 para batalhar, 2 para acessar a loja, 3 para usar poção, 0 para sair: ")

        if menu == "1":
            print("\nBatalha contra Goblin!")
            batalha(jogador, goblin)
            if goblin.esta_vivo() == False:
                jogador.ganhar_xp(goblin.xp_drop)
            
            print("\nBatalha contra Esqueleto!")
            batalha(jogador, esqueleto)
            if esqueleto.esta_vivo() == False:
                jogador.ganhar_xp(esqueleto.xp_drop)
            
            salvar_personagem(jogador)
            print("Jogo salvo!!")

        elif menu == "2":
            loja(jogador)

        elif menu == "3":
            jogador.usar_pocao()

        elif menu == "0":
            print("Saindo do jogo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()