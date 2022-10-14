# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

from random import randint
N = int(input("Введите размер списка: "))
lst = [randint(1, 10) for i in range(N)]
new_lst = []
print(f"{lst}")
for i in lst:
    if (not lst.count(i) > 1) and i not in new_lst:
        new_lst.append(i)

print(f"Список из неповторяющихся элементов: {new_lst}")
