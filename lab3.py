from math import *
x = 0.5
chisl = (1 + x)**((1 + x)**x)
znam = (1 - x)**((1 - x)**x)
logarifm = log10(x)
y = (chisl / znam) + logarifm
print(f"{y:.5f}")
