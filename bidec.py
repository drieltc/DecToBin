from time import sleep


def bindec(d, rest):
    sleep(0.5)
    print('Calculando a representação binária da parte decimal...')
    while(d != 0):

        # d é dobrado
        d = d*2
        # d is doubled

        # rest recebe a parte inteira de d
        rest.append(int(d))
        # rest receives the integer part of d

        # mostra d, apenas para conferir se tá pegando o valor certo
        sleep(0.5)
        print(f'{d} & {int(d)}')
        # prints d, just to check if the value it's getting is correct

        # diminui o tamanho de d em 1, caso d seja maior que 1
        if(d >= 1):
            d = d-1
        # reduces the value of d by 1, in case d is greater than 1

    print('\n')

    # retorna a lista rest, para que no arquivo 'separador'
    # a visualização seja feita da melhor maneira
    return rest
    # returns rest, so that in the 'separador' archive
    # the visualization be done correctly

# caso queira imprimir direto desse arquivo
    '''c = 0
    while (c < len(rest)):
        print(rest[c], end=' ')
        c = c+1
    print('\n')'''
# in case u wanto to print it direclty from here
