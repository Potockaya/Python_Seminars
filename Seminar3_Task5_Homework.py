# # Задайте число. Составьте список чисел Фибоначчи,
# # в том числе для отрицательных индексов.
# # Пример:
# # - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
# функция для расчета фибоначчи положительной части


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b


data = list(fibonacci(n))
# функция для расчета фибоначчи отрицательной части


def fibonacciminus(n):
    c, d = 1, -1
    for i in range(n):
        yield c
        c, d = d, c - d


dataminus = list(fibonacciminus(n))
# развернула список с минусовым фибоначчм
dataminus.reverse()
# добавила к развернотому 0
dataminus.append(0)
# dataminus.extend(data)
# соединила два списка
print(dataminus + data)
