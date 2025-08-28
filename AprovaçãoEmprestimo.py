print('================== APROVAÇÃO DE EMPRESTIMO ==================')
casa = float(input('Digite o valor da casa: €'))
salario = float(input('Digite seu salário: €'))
anos = int(input('Em quantos pretende quitar a casa: '))
print('=============================================================')
prestacao = casa / (anos * 12)
porcentagem = salario * 30 / 100
print('A prestação que será paga em {} anos é de {:.2f}€/mês'.format(anos, prestacao))
print('=============================================================')
if  prestacao <= porcentagem:
    print('\033[32mO empréstimo foi Aprovado!')
else:
    print('\033[31mO empréstimo foi Negado!')


