n = float(input('Digite uma distancia em metros: '))
cm = n  * 100
mm = n * 1000
dm = n * 10
dam = n / 10
hm = n / 100
km = n / 1000
print('Centimetros: {}\nMilímetros: {}\nDecímetro: {}\nDecâmetro: {}\nHectômetro: {}\nQuilômetro: {}'.format(cm, mm, dm, dam, hm, km))
