nome = input('Qual é o seu nome: ')
idade = input('Qual é a sua idade? ')
vip = input('Voce tem convite VIP? s/n: ')

idade = int(idade)


if idade >= 18 or vip == str.lower('s'):
    print('Voce pode entrar')
else:
    print('acesso negado')

