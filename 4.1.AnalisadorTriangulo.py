print('================= ANALISADOR DE TRIANGULO =================')
n = float(input('Primeiro segmento: '))
m = float(input('Segundo segmento: '))
p = float(input('Terceiro segmento: '))
print('===========================================================')

if n < m + p and m < n + p and p < n + m:
    print("\U00002705 \033[32mOs segmentos acima podem formar um triangulo\033[m \U00002705")
else:
    print("\U0000274C \033[31mOs segmentos inseridos não podem formar um triangulo\033[m \U0000274C")
