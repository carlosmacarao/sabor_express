x = int(input('Digite a cordenada x: '))

y = int(input('Digite a cordenada y: '))

if x and y > 0:
    print('Primeiro Quadrante!')

elif x < 0 and y > 0:
    print('Segundo Quadrante!')

elif x and y < 0:
    print('Terceiro Quadrante!')

else:
    print('Quarto Quadrante!')