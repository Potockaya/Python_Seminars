# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.142,    10 ^ (-1) ≤ d ≤10 ^ (-10)


# d = int(input("Введите число для заданной точности числа Пи:\n"))
# k = 2
# x = 6
# for i in range(1, 1000000):
#     x = x + (6/(k**2))
#     k = k+1
# print((x)**(1/2))


d = int(input("Введите число для заданной точности числа Пи:\n"))
k = 1
pileibnic = 0
for i in range(0, 1000000):
    if i % 2 == 0:
        pileibnic = pileibnic + 4/k
    else:
        pileibnic = pileibnic - 4/k
    k = k+2

print(round(pileibnic, d))
