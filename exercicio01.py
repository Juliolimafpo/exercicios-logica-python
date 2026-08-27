nome = input('Digite seu nome: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')

altura = float(altura)
peso = int(peso)

imc = peso / altura ** altura


print(f"{nome}Seu indice de massa corporal é: {imc}")