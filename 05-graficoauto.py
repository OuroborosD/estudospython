"""
script criado para pegar os dados de uma planilha, e gerar um grafico
#tarrefas
#pegar os dados da tabela

#separar em cada parte.
# criar uma função função para separar os dados.
# criar a função adcionar novos campos na tabela.
#salvar dados na tabela."""
import openpyxl as sheet
import matplotlib.pyplot as ptl
import numpy as np
letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
print(letras[1])
lista = []
rank = []
#carrega uma planilha já existente
dados = sheet.load_workbook('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\forças.xlsx')

#mostra os nomes das planilhas nessa folha.
nome_planilha = dados.sheetnames

#pega uma planilha, e referencia que todo o valor dela, estara numa variavel.
planilha1 = dados['Plan1']

#precisa ter o value, pois se não ele retorna o objeto. 
#que no caso seria a posição
print(planilha1['f16'].value)

#pega o valor que antes era 15.000 e salva como 22500
#planilha1['f16'] = 15000

for i in range(5,11,5):
    print(f'o valor é {i}')
    for j in range(0,10):
        #print(planilha1[f'{letras[i]}{j}'].value)
        
        #pegar os valores, da letra e do numero, e colocar numa variavel que vai por no
        #dicionario.
        lista.append(planilha1[f'{letras[i]}{j+16}'].value)
        
        if len(rank) < 10:
            rank.append(planilha1[f'B{j+2}'].value)
if len(lista) > 10:
     for i in range(5,11,5):
        for j in range(0,10):
            lista.append(planilha1[f'{letras[i]}{j+32}'].value)

print(rank)        
print(len(lista))

print('\n\n\n')

#for ranks in lista:#percorre todos os valores do dicionario.
 #   print(ranks)
#salva os dados que foram alterados ou adcionados.
#dados.save('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\forças.xlsx')


#classe = ['aprendiz', 'lutador', 'guerreiro', 'transedente', 'espirito menor','espirito maior','mestre espiritual','quase-lorde esp','lorde espirito','lorde','santo']
#real = [110000, 35000,6000,2500,800,90,13,4,0,0,0]

#dayne =[5000,15000,7000,4300,1300,260,25,4,1,0,0]

controle = len(lista)
incremento = 0
while controle != 0:
    dayne = []
    real = []
    for k in range(10):
        print(f'numero {k}  Dayne : {lista[k+incremento]} | familioha real : {lista[k+(20+incremento)]}')
        dayne.append(lista[k+incremento])
        real.append(lista[k+(20+incremento)])
    print(f'o valores da {dayne}')
    
    for l in range(0,9,3):
        t1 = dayne[l:l+3]
        t2 = real[l:l+3]
        c1 = rank[l:l+3]
        print(f'valor de l é:{l}  no {t1}')
        #largura da barra
        barWidth = 0.25

        #aumentado o grafico
        ptl.figure(figsize=(10,5))

        #posisão das barras
        r1 = np.arange(len(t1))
        r2 = [x + barWidth for x in r1]
        #caso tenha mais de dois graficos.
        # r3 = [x + barWidth for x in r2]

        #onde coloca as barras, todas coladas.
        #(1° espaço,2° dados,3° cor,4° tamanho,5° estiqueta.)
        ptl.bar(r1, t2, color = '#F51D4A', width=barWidth, label = 'familia real')
        ptl.bar(r2, t1, color = '#10DE6C',width=barWidth, label='house dayne')

        #a legenda do eixo X
        ptl.xlabel('ranks')
        #vai colocar o nome no eixo X, no caso as classes, nos grupos.
        #6° vai organizar as classes em cada grupo de valores, o antes e depois
        ptl.xticks([r+ barWidth for r in range(len(t2))], c1)

        #ptl.xticks([r+ barWidth for r in range(len(t1))], c1)

        #Carrega a legenda
        
        if controle == len(lista):
            for q in range(3):
                ptl.legend()
                if l == 0:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\inicio.png',format='png')
                elif l == 3:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\medio.png',format='png')
                else:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\avancado.png',format='png')
        else:
            for w in range(3):
                ptl.legend()
                if l == 0:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\inicio5.png',format='png')
                elif l == 3:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\medio5.png',format='png')
                else:
                    ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\avancado5.png',format='png')


   # if controle != len(lista):
    #    for p in range(10,19,3):

    incremento += int(len(lista)/4)
    controle -= len(lista)/2

