class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque 
        self.nivel = 1
        self.xp = 0
        self.pocoes = []
    

    def atacar(self, alvo):
        alvo.vida -= self.ataque
        print(f"{self.nome} causou {self.ataque} de dano!")

    def esta_vivo(self):
        return self.vida > 0
    
    
    def checar_nivel(self):
        xp_para_proximo = self.nivel * 50 
        if self.xp >= xp_para_proximo:
             while self.xp >= xp_para_proximo:
                self.xp -= xp_para_proximo
                self.nivel += 1
                self.vida += 20
                self.ataque += 5
                print(f"{self.nome} subiu para o nível {self.nivel}!")
             xp_para_proximo = self.nivel * 50

    def ganhar_xp(self, quantidade):
        self.xp += quantidade
        print(f"{self.nome} ganhou {quantidade} XP!")
        print(f"Nivel atual: {self.nivel}")
        self.checar_nivel()

    def usar_pocao(self):
        if not self.pocoes:
            print(f"{self.nome} não tem poções!")
            return  # <- retorna aqui apenas se não houver poções

        # Se tiver poção, aplica os efeitos
        pocao = self.pocoes.pop(0)
        self.vida += pocao.bonus_vida
        self.ataque += pocao.bonus_ataque
        print(f"{self.nome} usou {pocao.nome}!")
        print(f"Vida atual: {self.vida}, Ataque atual: {self.ataque}")
   