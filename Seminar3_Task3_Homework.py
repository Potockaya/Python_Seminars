# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20

from random import uniform
N = int(input("Введите размер списка: "))
lst = [round(uniform(1, 10), 2) for i in range(N)]
print(
    f"{lst} => {round(max(lst[i]%1 for i in range(len(lst))) - min(lst[i]%1 for i in range(len(lst))),2)}")
