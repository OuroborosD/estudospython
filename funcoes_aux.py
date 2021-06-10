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
            for i in range(int(((num+3)-1)*10),(num+3)*10):#para sempre pegar 10 listas
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
'''
