# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint
N = int(input("Введите размер списка: "))
lst = [randint(-10, 11) for i in range(N)]
lst2 = []
for i in range(len(lst)):
    while i < len(lst)/2 and N > len(lst)/2:
        N = N - 1
        a = lst[i] * lst[N]
        lst2.append(a)
        i += 1
print(lst)
print(lst2)
