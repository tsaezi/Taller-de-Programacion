# calcula producto punto
from math import sin

x = [1, 1, 1]


y = [2, 3, 3]

ppunto = 0

for i in range(len(x)):
    ppunto+=x[i]*y[i]
print(ppunto)