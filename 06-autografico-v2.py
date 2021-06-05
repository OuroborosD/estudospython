"""
Script para gerar pegar dados,e  gerar automaticamente na tabela-V1
#tarrefas
#pegar os dados da tabela
#separar em cada parte.
# criar uma função função para separar os dados.
# criar a função adcionar novos campos na tabela.
#salvar dados na tabela."""
import openpyxl as sheet
import matplotlib.pyplot as ptl
import numpy as np
from funcoes_aux import nome_imagem

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = []
rank = []
dados = sheet.load_workbook('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\forças.xlsx')#carrega os valores da planilha.
nome_planilha = dados.sheetnames
planilha1 = dados['Plan1']#nome da planilha que pega os dados.
path = "C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\"

for i in range(5,11,5):#esse loop é o que seleciona as letras. pula de 5 em 5.

    for j in range(0,10):#
        lista.append(planilha1[f'{letras[i]}{j+16}'].value)
        
        if len(rank) < 10:#entra se não tiver preenchido os ranks
            rank.append(planilha1[f'B{j+2}'].value)
            
if len(lista) > 10:
     for i in range(5,11,5):
        for j in range(0,10):
            lista.append(planilha1[f'{letras[i]}{j+32}'].value)

controle = len(lista)#controle ddo loop while
incremento = 0 #para pegar outros valores da tablema

while controle != 0:
    dayne = []
    real = []

    for k in range(10):
        dayne.append(lista[k+incremento])
        real.append(lista[k+(20+incremento)])
    
    for l in range(0,9,3):
        t1 = dayne[l:l+3]
        t2 = real[l:l+3]
        c1 = rank[l:l+3]
        print(f'valor de l é:{l}  no {t1}')
        barWidth = 0.25#largura da barra
        ptl.figure(figsize=(10,5))#aumentado o grafico

        #posisão das barras
        r1 = np.arange(len(t1))
        r2 = [x + barWidth for x in r1]
        #caso tenha mais de dois graficos.
        # r3 = [x + barWidth for x in r2]

        #onde coloca as barras, todas coladas.
        #(1° espaço,2° dados,3° cor,4° tamanho,5° estiqueta.)
        ptl.bar(r1, t2, color = '#F8D152', width=barWidth, label = 'familia real')#barra da familia real
        ptl.bar(r2, t1, color = '#382E63',width=barWidth, label='house dayne')#barra 
        ptl.xlabel('ranks')#a legenda do eixo X
        #vai colocar o nome no eixo X, no caso as classes, nos grupos.
        #6° vai organizar as classes em cada grupo de valores, o antes e depois
        ptl.xticks([r  + barWidth for r in range(len(t2))], c1)
        ptl.legend()
        referencia = len(lista)
        darnome = nome_imagem(controle,referencia,int(l/3))#o L é do loop for, que vai entrar na função e puxar a categoria do rank
        print(darnome)
        ptl.savefig(f'{path}{darnome}.png',format='png')
       
    incremento += int(len(lista)/4)#soma para adicionar o valor da numeração do valor de baixo.
    controle -= len(lista)/2#controle, para finalizar o while







