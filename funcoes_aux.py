import numpy as np
import matplotlib.pyplot as ptl
import random as r

def nome_imagem(controle,referencia,plus):#recebe os valores de controle é incremento.
    nomes = ['inicio','medio','avancado']
    retorno = ''
    if controle == referencia:
        retorno = nomes[plus]
        return retorno
    else:
        retorno = f'{nomes[plus]}5'
        return retorno

def nome_imagem_v2(plus,incremento):#recebe os valores de controle é incremento.
    nomes = ['inicio','medio','avancado']
    retorno = f'{nomes[plus]}{incremento}'
    return retorno

def nome_imagem_v3(plus,incremento,referencia,comp=0):#adicionado argumento opcional
    nomes = ['inicio','medio','avancado']
    sufix = ['d','r']
    retorno = ''
    ref = referencia/2
    if incremento != ref:
        retorno = f'{nomes[plus]}{incremento}'
        return retorno
    else:
        retorno = f'{nomes[plus]}{sufix[comp]}'
        return retorno

#tranformar uma lista em grupos de 10
def dividir_lista(num,lista=[],inc = 0):
    var= []
    if inc > 0 or num > 1:
        #print('entrou aqui')
        if inc != 0:
            for i in range(int(((num+4)-1)*10),(num+4)*10):#para sempre pegar 10 listas
                    var.append(lista[i])
                    #print(f'{i}  :  estou no inc segundo')

        else:            
            for i in range(int((num-1)*10),num*10):#para sempre pegar 10 listas
                var.append(lista[i])
               # print('estou no num >1')
                            
        return var

    else:
        for i in range(10):
            #print('estou no primeiro ---------------')
            var.append(lista[i])   
        return var

def quantidade_de_barras(barra,tamanho, qtd):
    #barra, éa referencia do tamanho que vai ter.
    #tamanho é a largura da barra. barwidth
    #qtd, numeros de barras
        barWidth = tamanho# chamei novamente para poder diminuit o tamanho
        lista = []
        r1 = np.arange(len(barra))#referencia
        lista.append(r1)
        for i in range(qtd):
            lista.append([x + barWidth for x in lista[i]])
        return lista



def barras_grafico(lista,grafico,barWidth,cor,qtd):
    #lista, o espaço entre as barras.
    #grafico, a lista com os dados
    # qtd, qunatos graficos tem
    # barwidth, lagura da barra.

    frases = ['começo','5 anos de exilio','depois, portoes de terã','Encontro no Abismo de Mael']
    lis= lista[qtd]
    gra = grafico[qtd]
    c = cor[qtd]
    fra =  frases[qtd]
    #bar = barWidth
    return ptl.bar(lis,gra , color = c ,width=barWidth, label = fra)


def cor(qtd):#funçao que pega a for autameticamente, dentro da lista.
    cor = ['#AECAF8','#AEF8D6','#B5EAF0','#F99DA5','#626DD9','#6A3AA6','#696273','#00A886','#9BD8DE','#62A6D9','#A83500']
    cor_aux = []#salvar as cores
    for i in range(0,qtd):
        cor_aux.append(cor[r.randint(0,len(cor))])
    return cor_aux
##################################TESTES###############################################
'''
#oi =nome_imagem_v3(0,30)
#print(oi)
aspas = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A B C D E F"
print(len(aspas))
index = aspas.index('Z')
print(index)
#t1,t2,t3 = dividir_lista(3,aspas,1),dividir_lista(2,aspas),dividir_lista(1,aspas)
#print(f'{t1}\n{t2}\n{t3}\n')
t1 = dividir_lista(2,aspas, 1)
print(t1)

aspas = ["A","B","C"]
teste_barra = tamanho_barra(aspas,0.24,6)
print(teste_barra[7])

aspas = ["A","B","C"]
barras_grafico(1,aspas,3,2)
'''
