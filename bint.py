from time import sleep


# só funciona se n for inteiro
# only works  if n is an integer
def binint(n, rest):
    sleep(0.5)
    print('Calculando a representação binária da parte inteira...')
    while(n >= 2):
        # a lista recebe o valor do resto da divisão de n por 2
        rest.append(n % 2)
        # the list receives the value of the rest of n divided by 2

        # mostra o valor de n e o resto da divisão (apenas para conferir)
        sleep(0.5)
        print(f'{n} & {n% 2}')
        # show the value of n and the rest of the division (just checking)

        # n se torna o próximo valor a ser calculado o resto da divisão
        n = int(n/2)
        # n becomes the next value to be calculated the rest of the division

    # não sei pq coloquei isso
    print(f'{n} = {n}')
    # not sure why I put this

    # a lista recebe o último valor que n se torna
    rest.append(n)
    # the list receives the last value n has became

    # retorna a lista rest, para que no arquivo 'separador'
    # a visualização seja feita da melhor maneira
    return rest
    # returns rest, so that in the 'separador' archive
    # the visualization be done correctly

    # caso queira imprimir direto desse arquivo
    '''print('\n')
    c = len(rest)-1
    while(c >= 0):
        print(rest[c], end=' ')
        c = c-1
    print('\n')'''
    # in case u wanto to print it direclty from here
