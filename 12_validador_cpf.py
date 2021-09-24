#TODO cria v2 identificar numeros repetidos, e quantidade de caracteres.

def verifica_repetido(valor,resultado = 0):
    """verifica se só tem numeros repetidos no cpf.
       modifiquei para uma igualdade, entre os valores multiplicados
       de  valor X ele mesmo e o resultado
       pois  pode dar um falso negativo. como o exemplo:
      o valor da 55, e 55 é divisivel por 11 com resto 0, ai dava erro.
      
     valor = 55 % 11 == 0  >> TRUE
    Args:
        valor string: os numeros do cpf
        resultado int: inicializa o resultado.

    Returns:
        bollean: verdedeiro ou falso dependendo se só tiver numeros repetidos
    """
    
    
    for i in range(len(valor)):
        resultado += int(valor[i])
    
    if resultado != (len(valor)*int(valor[0])):
        return True
    else:
        return False
            


def valida_cpf_v1(cpf):
    """função para validar cpf, irá verificar os ulitmos dois digitos.
       para saber se estão corretos

    Args:
        cpf (string): numeros do cpf

    Returns:
        bolean : se é valido ou não
    """
    verifica_cpf = cpf
    multiplicador = 10
    controle = 0
    digitos_verificadores = []

    while controle  != 2:
        valor = 0 # valor do incremento.
        
        for i in range((9+controle)):
            valor += int(verifica_cpf[i])*(multiplicador-i)
        resultado = valor*10%11
        
        if resultado == 10: #caso seja 10 o resto no cpf é 0 o digito
            resultado = 0 
        controle += 1 #incrementa para na proxima sair do loop
        multiplicador += 1 #incrementa para pegar o primeiro digito verificador na multiplicação.
        digitos_verificadores.append(resultado)

    if int(cpf[-2]) == digitos_verificadores[0] and int(cpf[-1]) == digitos_verificadores[1]:#foi transformado os para interiros
        return True                                          #pois estava dando erro comparando como string                   
    else:
        return False


def valida_cpf_v2(cpf):
    """valida cpf, consegue verificar os digitos, e se são numeros repetido


    Args:
        cpf (string): o valor do cpf

    Returns:
        dict: {'status': bolean, 'mensagem':'o por que do status'}
              retorna o booleano True ou False como o status, 
              e uma mensagem mostrando o por que o status.

    """
    verifica_cpf,multiplicador,controle,digitos_verificadores, = cpf, 10, 0, []
    mensagens = ['quantidade de digitos invalida','cpf invalido','todos os numeros não podem ser iguais','valido']
    retorno = {'valido':False, 'mensagem':mensagens[0]}#
    numeros_repetidos = verifica_repetido(verifica_cpf)

    if len(cpf) == 11 and numeros_repetidos == True  :
        while controle  != 2:
            valor = 0 # valor do incremento.
            for i in range((9+controle)):
                valor += int(verifica_cpf[i])*(multiplicador-i)
            resultado = valor*10%11
            if resultado == 10: #caso seja 10 o resto no cpf é 0 o digito
                resultado = 0 
            controle += 1 #incrementa para na proxima sair do loop
            multiplicador += 1 #incrementa para pegar o primeiro digito verificador na multiplicação.
            digitos_verificadores.append(resultado)

        if int(cpf[-2]) == digitos_verificadores[0] and int(cpf[-1]) == digitos_verificadores[1]:#foi transformado o cpf para interiro
                                                                                                 #pois estava dando erro comparando como string     
                retorno['mensagem'] = mensagens[3]
                retorno['valido'] = True
                return retorno
        else:
            retorno['mensagem'] = mensagens[1]
            return retorno
    elif numeros_repetidos:#caso não seja numero repetido entra aqui.
        
        return retorno
    else:
        retorno['mensagem'] = mensagens[2]
        return retorno






#23569741052 validos
#a3 = verifica_repetido('23569741052')
a4 = valida_cpf_v2('16951785805')
print(a4)