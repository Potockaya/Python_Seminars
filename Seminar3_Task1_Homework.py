# 1й вариант
from random import randint
N = int(input("Введите размер списка: "))
lst = [randint(-N, N+1) for i in range(N)]
summ = 0
for i in range(len(lst)):
    if i % 2 != 0:
        summ += lst[i]
print(
    f'Последовательность: {lst}-> на нечётных позициях элементы {lst[1]} и {lst[3]} Сумма: {summ}')

# 2й вариант
# from random import randint
# N = int(input("Введите размер списка: "))
# lst = [randint(-N, N+1) for i in range(N)]
# print(
#     f'Последовательность: {lst}-> на нечётных позициях элементы {lst[1]} и {lst[3]} Сумма: {sum(lst[1::2])}')
