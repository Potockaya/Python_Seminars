# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

# Примеры:

# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90


number1 = int(input('Введите первое число: '))
number2 = int(input('Введите второе число: '))
number3 = int(input('Введите первое число: '))
number4 = int(input('Введите второе число: '))
number5 = int(input('Введите первое число: '))
a = [number1, number2, number3, number4, number5]
maxNumber = max(a)
print(f'max = {maxNumber}')