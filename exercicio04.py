saldo = 500.0

nome = input('Digite seu nome: ')
saque = float(input('Quanto você quer sacar? '))


if saque <= 0:
    print('Valor inválido!')


elif saque > saldo:
    print('Saldo insuficiente!')


elif saque % 10 != 0:
    print('Erro: Este caixa só entrega notas de R$ 10 (digite valores como 20, 50, 100).')


else:
    saldo = saldo - saque
    print(f'Saque aprovado! Seu novo saldo é R$ {saldo}')