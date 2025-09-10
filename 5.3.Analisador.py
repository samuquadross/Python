somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for c in range (1, 5):
    print('========== {}ª Pessoa =========='.format(c))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

media = somaidade / 4
print('=====================================')
print('A média de idade do grupo é de \033[4;32m{:.2f}\033[0m'.format(media))
print('O homem mais velho é \033[4;32m{}\033[0m e possui \033[4;32m{}\033[0m anos'.format(nomevelho, maioridadehomem))
print('Existe \033[4;32m{}\033[0m mulher(es) com menos de \033[4;32m20\033[0m anos'.format(totmulher20))
