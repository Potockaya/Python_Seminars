# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
X = bool(input('Введите первое число 0 или 1: '))
Y = bool(input('Введите второе число 0 или 1: '))
Z = bool(input('Введите третье число 0 или 1: '))
if  not (X or Y or Z) == ((not X) and (not Y) and (not Z)):
    print (True)
else:
    print (False)
