"""
Script para gerar pegar dados,e  gerar automaticamente na tabela-V3
                                           
#pegar os dados da tabela                         V
#separar em cada parte.                           V  
# criar uma função função para separar os dados.  V
#função para tamanhos
# criar a função adcionar novos campos na tabela. X
#salvar dados na tabela.                          X  
# """

import openpyxl as sheet
import matplotlib.pyplot as ptl
import numpy as np
from funcoes_aux import nome_imagem_v3,dividir_lista,quantidade_de_barras,cor,barras_grafico,auto_label

letras = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lista = []
rank = []
dados = sheet.load_workbook('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\forças.xlsx')#carrega os valores da planilha.
nome_planilha = dados.sheetnames
planilha1 = dados['Plan1']#nome da planilha que pega os dados.
path = "C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\site\\STATIC\\IMG\\"

for i in range(5,26,5):#esse loop é o que seleciona as letras. pula de 5 em 5.
        if i < 26:
            for j in range(0,10):
                lista.append(planilha1[f'{letras[i]}{j+16}'].value)
                
                if len(rank) < 10:#entra se não tiver preenchido os ranks
                    rank.append(planilha1[f'B{j+2}'].value)
        else:
            for i in range(5,26,5):
                for j in range(0,10):
                    lista.append(planilha1[f'A{letras[i]}{j+16}'].value)

if len(lista) > 20:
     for i in range(5,26,5):
        for j in range(0,10):
            lista.append(planilha1[f'{letras[i]}{j+32}'].value)
else:
         for i in range(5,26,5):
            for j in range(0,10):
                lista.append(planilha1[f'A{letras[i]}{j+32}'].value)




controle = len(lista)#controle ddo loop while
referencia = len(lista)#referencia, que em tese nunca é para alterar o valor.
print(f'tamano da lista é {controle} | linha 43')
incremento = 0 #para pegar outros valores da tablema

while controle != 0:
    dayne = []
    real = []

    for k in range(10):
        #print(f'valor de k {k}° vez')
        #print(f'familia real {lista[k+incremento]} vez')
        dayne.append(lista[k+incremento])
        real.append(lista[k+int(referencia/2)+incremento])#onde começa ordem da familia real.
    
    for l in range(0,9,3):#vai do primeiro ao decimo item
        t1 = dayne[l:l+3]#pega os valores de 3 em 3.
        t2 = real[l:l+3]
        c1 = rank[l:l+3]
        barWidth = 0.25#largura da barra
        ptl.figure(figsize=(10,7))#aumentado o grafico
        ptl.rc('ytick', labelsize=20)#tamanho das informações no eixo Y 
        ptl.rc('xtick', labelsize=14)
        
        barras = quantidade_de_barras(t1,barWidth,2)

        #onde coloca as barras, todas coladas.
        #(1° espaço,2° dados,3° cor,4° tamanho,5° estiqueta.)
        ptl.bar(barras[1], t2, color = '#F8D152', width=barWidth, label = 'familia real')#barra da familia real
        ptl.bar(barras[2], t1, color = '#382E63',width=barWidth, label='house dayne')#barra 
        ptl.xlabel('ranks')#a legenda do eixo X
        #vai colocar o nome no eixo X, no caso as classes, nos grupos.
        #6° vai organizar as classes em cada grupo de valores, o antes e depois
        ptl.xticks([r  + barWidth for r in range(len(t2))], c1)
        ptl.legend()
        darnome = nome_imagem_v3(int(l/3),incremento,referencia)#o L é do loop for, que vai entrar na função e puxar a categoria do rank
        '''print(darnome)'''
        #auto_label(t1)
        ptl.savefig(f'{path}{darnome}.png',format='png')
       
    incremento += 10 #é o valor que vai contar.
    # incremento += int(len(lista)/4)#soma para adicionar o valor da numeração do valor de baixo.
    pid = int((len(lista)/10)/2)# alterar o valor do descremento do controle deacordo com o tamanho da lista.
    print(f'o pid é : {pid}')
    controle -= len(lista)/pid #decrementa o numero, para finalizar o while quando chegar a 0
    

    if controle == 0:#vai execultar um vez ao final do codigo, pois quando sai da subtração do controle  é a primeira vez que tem o valor de 0
        print('final do codigo-------------------------------')
        barWidth = 0.16
        qtd_barras = 5
        barras = quantidade_de_barras(t1,barWidth,qtd_barras)
        print(f'\n\n\n {barras[2]}\n\n\n')
        inc = 0
        cor_barra = cor(qtd_barras)#pega as cores, e fica salva a paleta com a quantidade certa.
        #mais = 0
        while inc < 2:
            for la in range(0,9,3):#vai do primeiro ao decimo item
                print(f' valor de la é {la}-----------------')
                tempo1,tempo2,tempo3,tempo4,tempo5,tempo6 = dividir_lista(1,lista,inc),dividir_lista(2,lista,inc),dividir_lista(3,lista,inc),dividir_lista(4,lista,inc),dividir_lista(5,lista,inc),dividir_lista(6,lista,inc)
                gra = []
                gra.append(tempo1[la:la+3])#pega os valores de 3 em 3.
                gra.append(tempo2[la:la+3])
                gra.append(tempo3[la:la+3])
                gra.append(tempo4[la:la+3])
                gra.append(tempo5[la:la+3])
                gra.append(tempo6[la:la+3])
                c2= rank[la:la+3]
            
                ptl.figure(figsize=(10,5))
                for i in range(0,qtd_barras):#servve para ficar chamando novas barras, automaticamente sem precisar completar
                    barras_grafico(barras,gra,barWidth,cor_barra,i)
                    #print(barras_grafico(barras,gra,barWidth,i))
              
                ptl.xlabel('ranks')#a legenda do eixo X
                #vai colocar o nome no eixo X, no caso as classes, nos grupos.
                #6° vai organizar as classes em cada grupo de valores, o antes e depois
                ptl.xticks([largura  + barWidth for largura in range(len(gra[1]))], c2)
                
                ptl.rc('ytick', labelsize=20)#tamanho das informações no eixo Y 
                ptl.rc('xtick', labelsize=14)
                ptl.legend()
                darnome = nome_imagem_v3(int(la/3),incremento,referencia,inc)#o L é do loop for, que vai entrar na função e puxar a categoria do rank
                print(darnome,' | linha 113')
                vamos_ver = 0
                if vamos_ver == 0:#coloquei dentro do if, pois só estava carregado o mesmo grafico.
                    print('vamos ver ',vamos_ver)
                    ptl.savefig(f'{path}{darnome}.png',format='png')
                    print('passou no save')
                    
                    vamos_ver += 1
            if la == 6:
                inc +=  1








