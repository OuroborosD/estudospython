def nome_imagem(controle,referencia,plus):#recebe os valores de controle é incremento.
    nomes = ['inicio','medio','avancado']
    retorno = ''
    if controle == referencia:
        retorno = nomes[plus]
        return retorno
    else:
        retorno = f'{nomes[plus]}5'
        return retorno

