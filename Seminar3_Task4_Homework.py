# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
binary = str()
number = int(input("Введите число:\n"))
while number != 0:
    binary = str(number % 2) + binary
    number //= 2
print(binary)
