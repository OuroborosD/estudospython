import matplotlib.pyplot as ptl
import numpy as np
#'aprendiz', 'lutador',110000, 35000,
classe = ['aprendiz', 'lutador', 'guerreiro', 'transedente', 'espirito menor','espirito maior','mestre espiritual','quase-lorde esp','lorde espirito','lorde','santo']
real = [110000, 35000,6000,2500,800,90,13,4,0,0,0]

dayne =[5000,15000,7000,4300,1300,260,25,4,1,0,0]

t1 = dayne[0:3]
t2 = real[0:3]
c1 = classe[0:3]
print(classe)
print(c1)
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
ptl.legend()
ptl.savefig('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\inicio.png',format='png')

