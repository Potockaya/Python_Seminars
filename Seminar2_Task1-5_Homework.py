# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

# мое решение
# n = (input('Введите число '))
# n = n.replace('-', '').replace('.', '').replace(',', '')
# sum_of_digit = sum(map(int, list(str(n))))
# print('Sum =', sum_of_digit)

# чужое решение с семинара
# def sum_digital_number(input_number):
#     sum_digit = 0
#     while input_number != 0:
#         sum_digit += input_number % 10
#         input_number //= 10
#     return sum_digit

# print(sum_digital_number(568))

# number = input('Введите число: ')
# number = number.replace('-', '').replace('.', '').replace(',', '')

# if number.isdigit():
#     sum_digits = sum_digital_number(int(number))
#     print(f'Сумма цифр числа равна: {sum_digits}')
# else:
#     print('Недопустимый ввод. Можно вводить только числа.')

# print(sum(int(i) for i in input('Введите вещественное число: ') if i.isdigit()))

# num = float(input('N: '))
# while int(num) != num:
#     num *= 10
# result = 0
# while num:
#     result += num % 10
#     num //= 10

# print(result)
# # 2. Напишите программу, которая принимает на вход число N и
# # выдает набор произведений чисел от 1 до N.
# # Пример:
# # пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите число N: '))
# res = 1
# for i in range(1, n+1):
#     res *= i
#     print(res, end=', ')

# #


# def factorial(input):
#     f = 1
#     for i in range(2, input + 1):
#         f *= i
#     return f
# print([
#     factorial(i) for i in range(1, int(input('N:')) + 1)
# ])
# #


# def fib(N):
#     if N == 1:
#         return N

#     return N * fib(N - 1)
# N = int(input('N: '))
# lst = []
# for i in range(1, N + 1):
#     lst.append(fib(i))

# print(lst)
# #
# def fib(N):
#     last = 1
#     for i in range(1, N + 1):  # 1 * 2 * 3 * 4
#         last *= i
#         yield last


# N = int(input('N: '))
# lst = list(fib(N))

# print(lst)
# print(lst)
# # 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n
# # и выведите на экран их сумму.

# # Пример:
# # 1 -> 2.0
# # 2 -> 4.25
# # 3 -> 6.62037037037037

# мое решение
# n = int(input('Введите число '))
# lst = [round((1+1/i)**i, 3) for i in range(1, n+1)]
# print(f'Последовательность: {lst}\nСумма: {round(sum(lst), 3)}')

# # 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# # Найдите произведение элементов на указанных позициях.
# # Позиции хранятся в файле file.txt в одной строке одно число.
# мое решение
from random import randint
N = int(input("Введите размер списка: "))
lst = [randint(-N, N+1) for i in range(N)]
print(lst)
result = 1
data = open('file.txt', 'r')
for line in data:
    if line == "" or int(line) > N:
        break
    result *= lst[int(line)]
data.close()
print(result)
# # 5. Реализуйте алгоритм перемешивания списка.
#  решение с семинара
# import random
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# random.shuffle(lst)
# print(lst)
