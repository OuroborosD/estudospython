lista = [
    [1,2,3,4,5,6,7,9,8,10],
    [1,3,3,4,5,6,7,8,9,10],
    [1,7,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10],
    [1,8,3,4,5,6,7,8,9,10],
]

def verificar(lista):
    ls = lista
    for index_lista in lista:
        for aux in index_lista:
            contador = 0
            for  lista in index_lista:
                print(f'aux : {aux}   lista: {lista}')
                if aux == lista:
                    
                    contador += 1
                    print('contaador ', contador)
                    if contador == 2:
                        ind = ls.index(index_lista)
                        print(f'no index da lista  numero {ind} o numero: {aux} se repete')
                        return 0
          #  print(aux)
        #print('============')

verificar(lista)