compra = input('Qual é o valor da compra? ')


compra = float(compra)

if compra <= 100:
    print(f'O valor da compra é R${compra}')
elif compra <= 500:
    valor = compra * 0.90
    desconto = compra - valor
    print(f'O valor da compra é R${valor} e o desconto foi de R${desconto}')
else:
    valor = compra * 0.80
    desconto = compra - valor
    print(f'O valor da compra é R${valor} e o desconto foi de R${desconto}')