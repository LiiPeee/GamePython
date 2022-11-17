import random

print("*********************************")
print("BEM VINDO AO JOGO DE ADIVINHAÇÃO!")
print("*********************************")

numero_secreto = random.randint(1,10)


tentativa = 3

chute_str = input("Digite o número: ")

chute = int(chute_str)

while(tentativa > 0):
    if(numero_secreto == chute):
        print("Você acertou")
        break
    elif(tentativa == 0):
        print("Você não acertou nenhuma das tentativas! BOCOOOZZAAUMMM")
        break
    print("Errou e tem {} tentativas".format(tentativa))
    tentativa -= 1
    chute = int(input("Digite novamente: "))