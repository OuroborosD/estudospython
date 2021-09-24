from random import randint as num

"""
1. Distrito Federal, Goiás, Mato Grosso do Sul e Tocantins;

2. Pará, Amazonas, Acre, Amapá, Rondônia e Roraima;

3. Ceará, Maranhão e Piauí;

4. Pernambuco, Rio Grande do Norte, Paraíba e Alagoas;

5. Bahia e Sergipe;

6. Minas Gerais;

7. Rio de Janeiro e Espírito Santo;

8. São Paulo;

9. Paraná e Santa Catarina;

0. Rio Grande do Sul.

"""
def gerador_cpf(estado = 10,  controle = 0):
    
    if estado != 10:
        return "em construção"
    
    digitos = str(num(000000000,999999999))
   
    incremento = 0
    while controle != 2:
        aux_conta = 0
        holder = 0
       
        for i in range(9+incremento):
            aux_conta += int(digitos[i]) * (10+incremento-i)
            
        
        #digitos_ver.append(int(aux_conta*10/11))
        holder = aux_conta*10%11
        digitos += str(holder)
        controle += 1 #incremento para sair o while.
        incremento = 1
    return digitos
    

    

gerador_cpf()
