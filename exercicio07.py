

print('Digite 3 lados de um triangulo')

lado_a = input('Digite o primeiro lado: ')
lado_b = input('Digite o segundo lado: ')
lado_c = input('Digite o terceiro lado: ')


if lado_a == lado_b and lado_b == lado_c:
    print('Esse triangulo é um equilatero')
elif lado_a != lado_b and lado_b != lado_c and lado_a != lado_c:
    print('Triangulo escaleno')
else:
    print('è um triangulo isoceles')