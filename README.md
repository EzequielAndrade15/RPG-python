# RPG Game in Python

Este projeto é um Jogo RPG desenvolvido em Python, utilizando Programação Orientada a Objetos (POO). O objetivo do jogo é oferecer uma experiência interativa onde o jogador pode criar seu personagem, enfrentar inimigos, ganhar experiência e adquirir itens em uma loja.

Tecnologias Utilizadas

Python 3.x

Programação Orientada a Objetos (POO)

Funções e Métodos

Funcionalidades


O jogo permite ao jogador realizar várias ações no mundo do RPG, incluindo:

Criação de Personagens

Batalhas Contra Inimigos

Uso de Poções

Compras na Loja





1. Criação de Personagens

O jogador pode criar um personagem de diferentes classes, como Guerreiro ou Mago, cada um com habilidades e atributos únicos. A função criar_personagem permite que o jogador escolha e personalize seu personagem.

2. Batalhas

O jogador pode batalhar contra inimigos como Goblin e Esqueleto. O combate é baseado nos atributos do personagem, como saúde, força e agilidade. Durante as batalhas, o jogador pode:

Ganhar experiência.

Adquirir itens, como poções.

3. Loja

A loja oferece itens valiosos, como poções, que podem ser compradas pelo jogador. As poções recuperam a saúde do personagem ou podem melhorar seus atributos. Os itens comprados são adicionados ao inventário e podem ser usados durante as batalhas.

4. Uso de Poções

As poções adquiridas na loja podem ser usadas para restaurar a saúde ou aumentar os atributos do personagem. Isso adiciona uma camada estratégica ao combate, pois o jogador deve decidir quando e como usar seus recursos de forma eficiente.




Estrutura do Código

O código é composto por diversas classes, funções e módulos que trabalham em conjunto para criar uma experiência de jogo fluida e dinâmica.





Arquivos Principais


main.py: Arquivo principal que contém a lógica do jogo, incluindo a interação com o jogador, batalhas, loja e o uso de poções.

personagem.py: Define a classe Personagem e seus atributos, métodos e ações.

inimigo.py: Define a classe Inimigo e os inimigos que o jogador enfrentará.

batalha.py: Contém a função batalha, que gerencia as interações durante os combates.

salvar.py: Funções para salvar e carregar o estado do jogador.

produto.py: Define os itens disponíveis na loja, como poções, com efeitos e preços.

classes.py: Contém as classes específicas de personagem, como Guerreiro e Mago, além da função para criar um novo personagem.
