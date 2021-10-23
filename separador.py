from bidec import bindec
from bint import binint
from time import sleep


def sepango(num):

    # lista dos valores guardados na análise da parte inteira
    listai = list()
    # list to store values on the integer part analysis

    # pi recebe a parte inteira do número fornecido
    pi = int(num)
    # pi receives the integer part of the given number

    # pd recebe a parte decimal do nḿero fornecido
    pd = num - pi
    # pd receives the decimal parte of the given number

    # mostra a parte inteira
    sleep(0.5)
    print(f'\nParte Inteira = {pi}')
    # shows the integer part

    # mostra a parte decimal
    sleep(0.5)
    print(f'Parte Decimal = {pd}\n')
    # shows the decimal part

    # caso pd seja diferente de 0
    # if pd is different than 0

    if(pd != 0):
        # lista dos valores guardados na análise da parte decimal
        listad = list()
        # list to store values on the decimal part analysis

        # rd recebe a representação binária da parte decimal
        rd = bindec(pd, rest=listad)
        # rd receives the binary representation of the decimal part

    # ri recebe a representação binária da parte inteira
    ri = binint(pi, rest=listai)
    # ri receives the binary representation of the integer part

    # mostrando o número completo em binário
    sleep(1)
    print('\nO número em binário é: \n')
    # showing the whole number in binary

    # primeiro mostrando a parte inteira; c recebe o valor da
    # última posição de ri, para percorrê-lo de trás para frente
    c = len(ri)-1
    # starting with the integer part; c receives the value
    # of ri's last position so it runs is from top to bottom

    # percorrendo ri de trás pra frente
    while(c >= 0):
        print(f'{ri[c]}', end='')
        c = c-1
    # going trhough ri from top to bottom

    # se a parte decimal existir, será mostrada
    if(pd != 0):
        print('.', end='')
        c = 0
        while (c < len(rd)):
            print(rd[c], end='')
            c = c+1
    # if the decimal part exists, it'll be shown

    print('\n')
