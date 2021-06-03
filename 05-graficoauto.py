import openpyxl as sheet

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
planilha1['f16'] = 15000

dados.save('C:\\Users\\snr\\OneDrive\\Documentos\\escritor\\forças.xlsx')
