import datetime
#o strftime, ira puxar só a hora do dia
hora = int(datetime.datetime.now().strftime('%H'))

if hora >=0 and hora <=11:
    print('bom dia')
elif hora >=12 and hora <=17:
    print('bom tarde')
if hora >=17 and hora <=23:
    print('bom noite')