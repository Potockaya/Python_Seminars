# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет
number1 = int(input('Введите первое число: '))
if 5>=number1 >=1:
    print ('нет')
elif 8>number1 >=6:
    print ('да')  
else:
    print ('такого дня недели не существует')