print('oi')
print('slasdlasd')
trava_lingua = 'o rato roeu a roupa do rei de roma'
#letra = input('digite a letra que quer que fica M: ')
letra = 'r'
novo_trava_lingua = ''
i = 0
print('oi')
if len(letra) == 1 and letra.isalpha:
    if trava_lingua.index(letra):
        while i < len(trava_lingua):
            if letra == trava_lingua[i]:
                novo_trava_lingua += trava_lingua.uppercase[i]

    else:
        print('letra não existe no trava lingua')
else:
    print('você não digitou uma letra ou digitou mais de uma')

print(novo_trava_lingua)
