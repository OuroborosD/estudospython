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

def nome_imagem_v3(plus,incremento):#recebe os valores de controle é incremento.
    nomes = ['inicio','medio','avancado']
    retorno = f'{nomes[plus]}{incremento}'
    return retorno


oi =nome_imagem_v2(0,0)
print(oi)



    


