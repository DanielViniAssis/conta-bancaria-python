#opções do menu
menu = """"
        BEM VINDO AO NOSSO BANCO

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
import time
import os

#Variaveis e Constante
saldo = 0
numero_depositos = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input (menu)
    os.system('cls')

    if opcao == "d":
        print ("          BEM VINDO AO DEPOSITO             ")
        time.sleep(1)
        while True:
            d = float (input("Digite o valor desejado para deposito: R$ "))
            if d <= 0:
                print("Valor invalido, insira um novo valor")
                time.sleep(3)
            else:
                extrato += f"Valor depositado: R$ {d:.2f}"
                print("Deposito realizado!")
                saldo += d
                time.sleep(3)
                os.system('cls')
                break
            
    elif opcao == "s":
        print("      BEM VINDO AO SAQUE    ")

        if numero_saques > LIMITE_SAQUES:
            print("Limites de saques diários já alcançados")
            continue

        s = int (input("Digite o valor para o saque: R$ "))
        if s > limite:
            print("Limite de valor para saque alcançado")
            time.sleep(2)
            os.system('cls')
            continue
        if s > saldo:
            print("Saldo insuficiente para saque!")
        else:
            print("Contando as cedulas", end="")
            for i in range(3):
                print(".", end="", flush=True)
                time.sleep(0.5)
            print("Saque realizado!")
            saldo -= s
            time.sleep(1)
            print(f"Saldo: R${saldo}")
            time.sleep(2)
            numero_saques += 1
            extrato += f"Saque: R$ {s: .2f}"
            os.system('cls')
    
    elif opcao == "e":
        print("       BEM VINDO AO EXTRATO       ")
        print("Não ocorreu movimentações bancarias" if not extrato else extrato)
        print(f"Saldo: R$ {saldo: .2f}")
        time.sleep(2)
        os.system('cls')
    elif opcao == "q":
        break
    
    else: 
        print("Opção invalida, escolha uma valida") 
    