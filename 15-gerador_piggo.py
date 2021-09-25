from random import randint as rd, choice, random, uniform, choices
pessoa = ['sumaria','quejose','xoao','wilucas','thwiagthon','diogo','diego','ester','lilas','mormom']

tipo_pagamento = ['credito','debito/dinheiro','boleto','pix']
tipo_despesa = ['conta','compra Online','mercado','lanche']
descricao = 'asdszxczxcxcmweqwefsadszxckledsddsdaxcqwerasdghjk'


def usuario(lista_pessoa):
    pessoa = lista_pessoa
    for i in pessoa:
        with open('piggodados.sql','a') as piggo_usuario:
            piggo_usuario.write( f'''INSERT INTO 
                usuario(usuario_nome,usuario_login,usuario_fechamento)
                VALUES
            ('{i}','{i}',{rd(1,28)});\n''')


def despesa(tipo_pagamento,tipo_despesa, pessoas):
    for i in range(0,10000):    
        descricao1 = ''.join(choices(descricao, k=10))  # Gera nomes de tamanho 10
        pagamento = choice(tipo_pagamento)
        despesa  = choice(tipo_despesa)
        valor =  round(uniform(10,1000),2)
        mes =str(rd(1,9))
        mes = mes.zfill(2)# preenche com 0, caso só tenha um digito.
        dia = str(rd(1,28))
        dia = dia.zfill(2)
        data = f'{dia}-{mes}-2021'
        pessoa =rd(1,len(pessoas))
        with open('piggodados.sql','a') as piggo_despesa:
             piggo_despesa.write (f'''INSERT INTO
                despesa(despesa_data,despesa_descricao,despesa_meio_pagamento,despesa_tipo_despesa,despesa_recorrencia, despesa_valor,despesa_usuario_id)
            VALUES
                ('{data}','{descricao1}','{pagamento}','{despesa}',FALSE,{valor},{pessoa});''')
contador = 0
for i in range(600):
    variavel = rd(1,len(pessoa))
    if variavel == 11:
        contador += 1
        
print(contador)

valor1 = random()
print(valor1,5*valor1)
valor2 =  round(uniform(10,1000),2)


#usuario(pessoa)
despesa(tipo_pagamento,tipo_despesa,pessoa)
