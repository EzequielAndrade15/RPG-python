import json

def salvar_personagem(personagem, arquivo="save.json"):
    dados = {
        "nome": personagem.nome,
        "vida": personagem.vida,
        "ataque": personagem.ataque,
        "nivel": personagem.nivel,
        "xp": personagem.xp
    }
    with open(arquivo, "w") as f:
        json.dump(dados, f)



def carregar_personagem(arquivo="save.json"):
    import json
    with open(arquivo, "r") as f:
        dados = json.load(f)
    from personagem import Personagem
    jogador = Personagem(
        nome=dados["nome"],
        vida=dados["vida"],
        ataque=dados["ataque"]
    )
    jogador.nivel = dados["nivel"]
    jogador.xp = dados["xp"]
    return jogador