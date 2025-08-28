p = float(input('Informe seu peso atual: '))
a = float(input('Informe sua altura: '))
imc = p / a ** 2
print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print("\033[31mVocê está abaixo do peso!")
elif imc >= 18.5 and imc <= 25:
    print('\033[32mVocê está no peso ideal!')
elif imc >= 25 and imc <= 30:
    print('\033[33mVocê está sobrepeso!')
elif imc >= 30 and imc <= 40:
    print('\033[31mVocê está em obesidade!')
elif imc >= 40:
    print('\033[1;4;31mVocê está em obesidade mórbida!')
