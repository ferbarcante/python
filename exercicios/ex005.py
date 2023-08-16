idade = int(input('Qual a sua idade?'))
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))

if idade >= 18 and peso >= 60 and altura >= 1.70:
    print('Voce está apto a ir ao exército')
else:
    print('Voce não está apto a ir ao exército')
