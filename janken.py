import random
opcoes = ["pedra", "papel", "tesoura"]
modo1 = False
modo2 = False
modo3 = False

def continuar():
    continuar = int(input("1 para continuar 2 para parar: "))
    if continuar == 2:
        modo3 = False
        opcaoJogo = int(input(
            "Escolha uma modalidade: 1 para Jogador x Jogador, 2 para Jogador x Computador ou 3 para Computador x Computador: "))

opcaoJogo = int(input("Escolha uma modalidade: 1 para Jogador x Jogador, 2 para Jogador x Computador ou 3 para Computador x Computador: "))
if opcaoJogo == 1:
    modo1 = True
elif opcaoJogo == 2:
    modo2 = True
elif opcaoJogo == 3:
    modo3 = True
else:
    print("Opção Inválida")

while(modo1):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    comp1 = opcoes[x]
    comp2 = opcoes[y]
    print("O jogador escolheu {}".format(comp1))
    print("O computador escolheu {}".format(comp2))
    if comp1 == "pedra":
        if comp2 == "papel":
            print("Voce perdeu! papel bate pedra")
        elif comp2 == "tesoura":
            print("Voce ganhou! pedra bate tesoura")
        else:
            print("Empate!")
    continuar()

while(modo2):
    x = random.randint(0, 2)
    jogador = input("Escolha pedra, papel ou tesoura: ")
    comp = opcoes[x]
    print("O jogador escolheu {}".format(jogador))
    print("O computador escolheu {}".format(comp))
    if jogador == "pedra":
        if comp == "papel":
            print("Voce perdeu! papel bate pedra")
        elif comp == "tesoura":
            print("Voce ganhou! pedra bate tesoura")
        else:
            print("Empate!")
    if jogador == "papel":
        if comp == "tesoura":
            print("Voce perdeu! tesoura bate papel")
        elif comp == "pedra":
            print("Voce ganhou! papel bate pedra")
        else:
            print("Empate!")
    if jogador == "tesoura":
        if comp == "pedra":
            print("Computador 2 ganhou! pedra bate tesoura")
        elif comp == "papel":
            print("Computador 1 ganhou! tesoura bate papel")
        else:
            print("Empate!")
    continuar()

while(modo3):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    comp1 = opcoes[x]
    comp2 = opcoes[y]
    print("O Computador 1 escolheu {}".format(comp1))
    print("O Computador 2 escolheu {}".format(comp2))
    if comp1 == "pedra":
        if comp2 == "papel":
            print("Computador 2 ganhou! papel bate pedra")
        elif comp2 == "tesoura":
            print("Computador 1 ganhou! pedra bate tesoura")
        else:
            print("Empate!")
    if comp1 == "papel":
        if comp2 == "tesoura":
            print("Computador 2 ganhou! tesoura bate papel")
        elif comp2 == "pedra":
            print("Computador 1 ganhou! papel bate pedra")
        else:
            print("Empate!")
    if comp1 == "tesoura":
        if comp2 == "pedra":
            print("Computador 2 ganhou! pedra bate tesoura")
        elif comp2 == "papel":
            print("Computador 1 ganhou! tesoura bate papel")
        else:
            print("Empate!")
    continuar()
