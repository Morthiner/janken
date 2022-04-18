# 3 modalidades escolhidas no inicio P x P, P x C, C x C
# Cada partida coleta a opçao escohida pelo jogador, no caso de jogada do computador a opção é escolhida aleatoriamente
# O jogo tem inumeras partidas e no final de cada partida o jogador tem a opçao de CONTINUAR ou SAIR
# Caso o jogador saia o programa deve exibir um placar e uma mensagem de agradecimento com uma mensagem de 
    # agradecimento com os nomes dos estudantes


import random
opcoes = ["pedra", "papel", "tesoura"]

# Função jogada do computador => computador()
def computador():
    x = random.randint(0,2) 
    return opcoes[x]

# Função jogada do jogador => jogador()
def jogador():
    opcaoJogador = input("Escolha pedra, papel ou tesoura: ")
    return opcaoJogador
    #y = random.randint(0,2)
    #return opcaoJogador

temp = True

while(temp):
    if jogador() == "pedra":
        print("Jogador escolheu {}".format(jogador()))
        if computador() == "papel":
            print("Computador escolheu {}".format(computador()))
            print("Papel bate pedra, Jogador perdeu!")
        elif computador() == "tesoura":
            print("Computador escolheu {}".format(computador()))
            print("Pedra bate tesoura, Jogador ganhou!")
        else:
            print("Computador escolheu {}".format(computador()))
            print("Empate!")
    #print("Jogador escolheu {}".format(jogador()))
    continuar = int(input("Para CONTINUAR digite 1 e para SAIR digite 2: "))
    if continuar == 2:
        temp = False 


