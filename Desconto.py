n = float(input('Preço do produto: '))
desconto = 5
s = n - (n * desconto / 100)
print('O preço do produto com 5% de desconto é: {} €'.format(s))