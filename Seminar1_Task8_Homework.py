# Напишите программу, которая принимает на вход координаты точки 
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

X = int(input('Введите координату X: '))
Y = int(input('Введите координату Y: '))
if X>0 and Y>0:
    print("первая четверть")
elif X < 0 and Y > 0:
    print('вторая четверть')
elif X < 0 and Y < 0:
    print('третья четверть')
elif X > 0 and Y < 0:
    print('четвертая четверть')    
