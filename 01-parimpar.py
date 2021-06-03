numero = input('digite um numero interio')

if numero.isdecimal():
    num = int(numero)%2
    if num == 0:
        print(f'o numero: {numero} é par')
    else:
        print(f'o numero: {numero} é impar')
else:
    print('você não digitou um numero!')