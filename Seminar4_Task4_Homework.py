# 4. Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff = [randint(0, 101) for i in range(k)]+[randint(1, 101)]
poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
                j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly = poly.replace('x^1+', 'x+')
poly = poly.replace('x^0', '')
poly += ('', '1')[poly[-1] == '+']
poly = (poly, poly[:-2])[poly[-2:] == '^1']
print(poly)


my_file = open("Task4.txt", "w")
my_file.write(poly)
my_file.close()
