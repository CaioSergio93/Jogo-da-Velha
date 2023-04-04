import os
import random
from colorama import Fore, Back, Style

jogarNovamente="s"
jogadas=0
quemJoga=2 # 1 - CPU 2 - PLAYER
maxJogadas=9
velha=[
    [" ", " ", " "], # L0CO L0C1 L0C2
    [" ", " ", " "], # L1C0 L1C1 L1C2
    [" ", " ", " "]  # L2C0 L2C1 L2C2
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("   -----------")
    print("Jogadas: " + Fore.BLUE +  str(jogadas) + Fore.RESET)

def jogadorJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    
    if quemJoga==2 and jogadas<maxJogadas:
        l=int(input("Linha...: "))
        c=int(input("Coluna..: "))
        
        try:
            while velha [l][c]!= " ":
                l=int(input("Linha...: "))
                c=int(input("Coluna..: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha e/ou coluna invalida")
            
def cpuJoga():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha[l][c]!=" ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[l][c]="O"
        jogadas+=1
        quemJoga=2
        
def verificarVitoria():
    global velha
    vitoria = "n"
    simbolos = ["X", "O"]
    for s in simbolos:
        # Verificar Linhas
        for il in range(3):
            soma = 0
            for ic in range(3):
                if velha[il][ic] == s:
                    soma += 1
            if soma == 3:
                vitoria = "s"
                break

        # Verificar Colunas
        if vitoria == "n":
            for ic in range(3):
                soma = 0
                for il in range(3):
                    if velha[il][ic] == s:
                        soma += 1
                if soma == 3:
                    vitoria = "s"
                    break

        # Verificar diagonais
        if vitoria == "n":
            soma = 0
            for i in range(3):
                if velha[i][i] == s:
                    soma += 1
            if soma == 3:
                vitoria = "s"

        if vitoria == "n":
            soma = 0
            for i in range(3):
                if velha[i][2 - i] == s:
                    soma += 1
            if soma == 3:
                vitoria = "s"
                break
                
    return vitoria
                                     
while True:
    tela()
    jogadorJoga()
    cpuJoga()
    vitoria = verificarVitoria()
    if vitoria == "s":
        tela()
        print(Fore.RED + "Fim de Jogo!" + Fore.RESET)
        break
    if jogadas>=maxJogadas:
        tela()
        print("Empate!")
        break
 