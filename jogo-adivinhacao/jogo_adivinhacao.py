# JOGO ADIVINHAÇÃO FEITO EM PYTON 

nivel_dificuldade =[
    {"Fácil", 10},
    { "Médio", 5},
    { "Difícil", 3}
]   

import random

def jogo_adivinhacao():

    print("Selecione a dificuldade: ")
    for i, (nome, tentativas) in enumerate(nivel_dificuldade, start=1):
        print(f"{i}. {nome} - {tentativas} tentativas")

    while True:
        try:
            escolha = int(input("Digite o número da dificuldade: "))
            if 1 <= escolha <= len(nivel_dificuldade):
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Escolha inválida. Tente novamente.")


    nivel_escolhido = nivel_dificuldade[escolha - 1]

    numero_secreto = random.randint(1, 10)

    limite_tentativas = nivel_escolhido[1]

    tentativas = 0
    while tentativas < limite_tentativas:

        while True:
            try:
                adivinhacao = int(input("Adivinhe o número secreto (entre 1 e 10): "))
                if 1 <= adivinhacao <= 10:
                    break
                else:
                    print("Adivinhação inválida. Tente novamente.")
            except ValueError:
                print("Adivinhação inválida. Tente novamente.")

        if adivinhacao == numero_secreto:
            print("Parabéns! Você acertou o número secreto!")
        elif adivinhacao < numero_secreto:
            print("O número secreto é maior que o seu palpite")
        else:
            print("O número secreto é menor que o seu palpite")


        tentativas += 1
    if tentativas == limite_tentativas:
        print(f"Você não acertou o número secreto. O número secreto era {numero_secreto}.")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        jogo_adivinhacao()

jogo_adivinhacao()

