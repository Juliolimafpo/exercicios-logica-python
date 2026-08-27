ano_atual = input('Em que ano estamos: ')

ano_atual = int(ano_atual)

if ano_atual % 4 == 0 and ano_atual % 100 != 0 or ano_atual % 400 == 0:
    print('Esse ano é bissexto')
else:
    print('Nao é bissexto')