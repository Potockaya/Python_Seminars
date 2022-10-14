# 2. Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

num = int(input('Введите число '))
lst_simple = []
simple = 2
while num > 1:
    if num % simple == 0:
        lst_simple.append(simple)
        num = num/simple
    else:
        simple += 1
if len(lst_simple) == 1:
    print('число простое само по себе')
print(lst_simple)
