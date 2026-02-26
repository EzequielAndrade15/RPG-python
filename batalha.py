def batalha(jogador, inimigo):
    print(f"{jogador.nome} X {inimigo.nome}")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.atacar(inimigo)
        if inimigo.esta_vivo():
            inimigo.atacar(jogador)

    if jogador.esta_vivo():
        print("Voce venceu!!")
        jogador.xp += inimigo.xp_drop
        print(f"{jogador.xp}")
        jogador.vida = 20
    else:
        print("Voce perdeu")