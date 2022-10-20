# 2 – Дана последовательность чисел. Получить список
# уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint

N = int(input("Введите размер списка: "))
lst = [randint(1, 10) for i in range(N)]
new_lst = []
print(f"{lst}")
for i in lst:
    if (not lst.count(i) > 1) and i not in new_lst:
        new_lst.append(i)

print(f"Список из неповторяющихся элементов: {new_lst}")

new_lst2 = []
for i in lst:
    if (lst.count(i) > 1) and i not in new_lst2:
        new_lst2.append(i)
print(f"Список из повторяющихся элементов: {new_lst2}")

new_lst3 = []
for i in lst:
    if (lst.count(i) >= 1) and i not in new_lst3:
        new_lst3.append(i)
print(f"Список без дуюликатов: {new_lst3}")
