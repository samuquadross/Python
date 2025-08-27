print('============ ANALISADOR DE TRIANGULO ===========')
n = float(input('Primeiro segmento: '))
m = float(input('Segundo segmento: '))
p = float(input('Terceiro segmento: '))
print('================================================')

if n < m + p and m < n + p and p < n + m:
    print("\U00002705 Os segmentos acima podem formar um triangulo \U00002705")