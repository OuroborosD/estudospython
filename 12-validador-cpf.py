#TODO cria v2 identificar numeros repetidos, e quantidade de caracteres.

def verifica_repetido(valor):
    """verifica se só tem numeros repetidos no cpf.
       modifiquei para uma igualdade, entre os valores multiplicados
       pois  pode dar um falso negativo. como o exemplo:

    Args:
        valor string: os numeros do cpf

    Returns:
        bollean: verdedeiro ou falso dependendo se só tiver numeros repetidos
    """
    numero = valor
    resultado = 0
    for i in range(len(numero)):
        resultado += int(numero[i])
        print(resultado)
    if resultado % len(numero) != 0:
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
    verifica_cpf,multiplicador,controle,digitos_verificadores, = cpf,10,0,[],
    mensagens = ['quantidade de digitos invalida','cpf invalido','todos os numeros não podem ser iguais']
    retorno = {'valido':False, 'mensagem':mensagens[0]}#
    numeros_repetidos = verifica_repetido(verifica_cpf)
    print(f'resultado {numeros_repetidos}')
    if len(cpf) == 11   :
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
    
    return retorno







a3 = verifica_repetido('23569741052')
a4 = verifica_repetido('11111111111')
print(a4,"\n")