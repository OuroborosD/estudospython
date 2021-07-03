numero = '12345678912'


def formatar_cpf(cpf):
    """gera uma mascara, usando as mascaras, ou a função format.
    
    #os %s são são conversores servem para converter tudo que está lá em String
    #o %  são flags, marca onde termina os conversores e onde é para ser colocado os numeros para formatar
    Args:
        cpf ([string]): os 11 digitos do cpf

    Returns:
        [string]: valor formatado 123.456.789-12
    """
    return "%s.%s.%s-%s" % (cpf[:3], cpf[3:6],cpf[6:9],cpf[9:])
    
    # ou poderia usar o metodo format  
    oi = '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6],cpf[6:9],cpf[9:])
                                                        
pessoa = formatar_cpf(numero)
print(pessoa)
