nome = input('Qual é o seu nome? ')
salario = input('Qual é o seu salario? ')
parcela = input('Qual é o valor das parcelas? ')


salario = float(salario)
parcela = float(parcela)

porcentagem = salario * 0.30

if porcentagem >= parcela:
    print(f'Parabens {nome} seu emprestimo foi aprovado!!!')

else: 
    print(f'Erro Sr {nome} seu emprestimo nao pode ser aprovado pois as parcelas passam dos 30% do salario')
    