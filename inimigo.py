from personagem import Personagem

class Inimigo(Personagem):
    def __init__(self, nome, vida, ataque, xp_drop):
        super().__init__(nome, vida, ataque)
        self.xp_drop = xp_drop