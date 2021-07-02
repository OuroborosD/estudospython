def valida_cpf(cpf):
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
    lista = []
    while controle  != 2:
        valor = 0 # valor do incremento.
        for i in range((9+controle)):
            valor += int(verifica_cpf[i])*(multiplicador-i)
        resultado = valor*10%11
        if resultado == 10: #caso seja 10 o resto no cpf é 0 o digito
            resultado = 0 
        controle += 1
        multiplicador += 1
        lista.append(resultado)
    if int(cpf[-2]) == lista[0] and int(cpf[-1]) == lista[1]:#foi transformado os para interiros
        return True                                          #pois estava dando erro comparando como string                   
    else:
        return False

a1 = valida_cpf('06159198394')
print(a1)
