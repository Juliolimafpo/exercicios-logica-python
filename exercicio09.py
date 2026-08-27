nome = input('Seu nome: ')
idade = input('Sua idade: ')
renda = input('Sua renda: ')

idade = int(idade)
renda = float(renda)

if idade >= 18 and renda >= 2000:
    print(f'Parabens {nome}, beneficio aprovado')
else:
    print('Voce Nao atende os requisitos, Renda minima R$2000 e ser maior de idade')


