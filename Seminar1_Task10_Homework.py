# Напишите программу, которая принимает на вход координаты 
# двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
AX = int(input('Введите координату X точки A: '))
AY = int(input('Введите координату Y точки A: '))
BX = int(input('Введите координату X точки B: '))
BY = int(input('Введите координату Y точки B: '))
d= (((AX-BX)**2)+((AY-BY)**2))**(1/2)
print (round(d,2))