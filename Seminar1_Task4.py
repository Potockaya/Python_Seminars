# Напишите программу, которая будет принимать на вход дробь 
# и показывать первую цифру дробной части числа.

# Примеры:

# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3

n = float(input('Введите целое число: '))
m = int (n*10)%10
if m == 0:
    print ('нет')
else:
    print(m)