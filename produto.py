class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao



class Pocao(Produto):
    def __init__(self, nome, preco, descricao, bonus_vida, bonus_ataque):
        super().__init__(nome, preco, descricao)
        self.bonus_vida = bonus_vida
        self.bonus_ataque = bonus_ataque
 
 
def comprar(jogador, produto):
    """
    Adiciona a poção ao inventário do jogador.
    """
    if not hasattr(jogador, "pocoes"):
        jogador.pocoes = []  # cria a lista se não existir
    
    jogador.pocoes.append(produto)
    print(f"{produto.nome} comprado com sucesso! Você agora tem {len(jogador.pocoes)} poções.")