nome_aluno = input('Digite o nome do aluno: ')
nota1 = input('digite a primeira nota: ')
nota2 = input('digite a segunda nota: ')
nota3 = input('digite a terceira nota: ')

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Aluno {nome_aluno} aprovado!')
elif media >= 4:
    print(f'Aluno {nome_aluno} está de recuperação!')
else:
    print(f'Aluno {nome_aluno} Reprovado')