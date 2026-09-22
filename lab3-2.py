from math import *
a = -0.3
b = 0.7
n = 0.05
shag = int((b-a) / n) + 1
for i in range(shag):
    x = a + i * n
    numb1 = sqrt((2**x + x**2) / (1 - 2 * (x**2)))
    numb2 = sqrt((cos(x) - sin(x)) / (sin(x) + cos(x)))
    y = numb1 + numb2
    print(f"{x:.5f}", f"{y:.5f}")
