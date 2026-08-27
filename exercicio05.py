velocidade = input('Velocidade do veiculo: ')


limite = 80


velocidade = float(velocidade)

if velocidade <= limite:
    print('Voce esta no limite pode prosseguir!!')
elif velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7.0
    print(f'Voce ultrapassou {velocidade} o limite, sua multa é {multa}')