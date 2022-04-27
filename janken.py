import random
opcoes = ["pedra", "papel", "tesoura"]
modo1 = False
modo2 = False
modo3 = False

def continuar():
    continuar = int(input("1 - Continuar \n2 - Parar\n> "))
    if continuar == 2:
        global modo1
        modo1 = False 
        global modo2
        modo2 = False
        global modo3
        modo3 = False
        global opcaoJogo
        opcaoJogo = int(input(
            "Escolha uma modalidade: \n1 - Jogador x Jogador \n2 - Jogador x Computador \n3 - Computador x Computador\n> "))
        if opcaoJogo == 1:
            modo1 = True
        elif opcaoJogo == 2:
            modo2 = True
        elif opcaoJogo == 3:
            modo3 = True
        else:
            print("Opção Inválida")
opcaoJogo = int(input(
            "Escolha uma modalidade: \n1 - Jogador x Jogador \n2 - Jogador x Computador \n3 - Computador x Computador\n> "))
if opcaoJogo == 1:
    modo1 = True
elif opcaoJogo == 2:
    modo2 = True
elif opcaoJogo == 3:
    modo3 = True
else:
    print("Opção Inválida")
while True:
    while(modo1):
        comp1 = input("Escolha pedra, papel ou tesoura: ")
        comp2 = input("Escolha pedra, papel ou tesoura: ")
        print("O Jogador 1 escolheu {}".format(comp1))
        print("O Jogador 2 escolheu {}".format(comp2))
        print("-" * 50)
        if comp1 == "pedra" and comp2 == "papel":
                print("O Jogador 2 ganhou! papel bate pedra")
        elif comp1 == "papel" and comp2 == "pedra":
                print("O Jogador 1 ganhou! papel bate pedra")
        elif comp1 == "tesoura" and comp == "pedra":
                print("O Jogador 2 ganhou! pedra bate tesoura")
        elif comp1 == "pedra" and comp2 == "tesoura":
                print("O Jogador 1 ganhou! pedra bate tesoura")
        elif comp1 == "papel" and comp2 == "tesoura":
                print("O Jogador 2 ganhou! tesoura bate papel")
        elif comp1 == "tesoura" and comp2 == "papel":
                print("O Jogador 1 ganhou! tesoura bate papel")
        else:
            print("Empate!")
        print("-" * 50)
        continuar()

    while(modo2):
        x = random.randint(0, 2)
        jogador = input("Escolha pedra, papel ou tesoura: ")
        comp = opcoes[x]
        print("O jogador escolheu {}".format(jogador))
        print("O computador escolheu {}".format(comp))
        print("-" * 50)
        if jogador == "pedra" and comp == "papel":
                print("Voce perdeu! papel bate pedra")
        elif jogador == "papel" and comp == "pedra":
                print("Voce ganhou! papel bate pedra")
        elif jogador == "tesoura" and comp == "pedra":
                print("Voce perdeu! pedra bate tesoura")
        elif jogador == "pedra" and comp == "tesoura":
                print("Voce ganhou! pedra bate tesoura")
        elif jogador == "papel" and comp == "tesoura":
                print("Voce perdeu! tesoura bate papel")
        elif jogador == "tesoura" and comp == "papel":
                print("Voce ganhou! tesoura bate papel")
        else:
            print("Empate!")
        print("-" * 50)
        continuar()

    while(modo3):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        comp1 = opcoes[x]
        comp2 = opcoes[y]
        print("O Computador 1 escolheu {}".format(comp1))
        print("O Computador 2 escolheu {}".format(comp2))
        print("-" * 50)
        if comp1 == "pedra" and comp2 == "papel":
                print("O Computador 2 ganhou! papel bate pedra")
        elif comp1 == "papel" and comp2 == "pedra":
                print("O Computador 1 ganhou! papel bate pedra")
        elif comp1 == "tesoura" and comp2 == "pedra":
                print("O Computador 2 ganhou! pedra bate tesoura")
        elif comp1 == "pedra" and comp2 == "tesoura":
                print("O Computador 1 ganhou! pedra bate tesoura")
        elif comp1 == "papel" and comp2 == "tesoura":
                print("O Computador 2 ganhou! tesoura bate papel")
        elif comp1 == "tesoura" and comp2 == "papel":
                print("O Computador 1 ganhou! tesoura bate papel")
        else:
            print("Empate!")
        print("-" * 50)
        continuar()
