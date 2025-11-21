from math import sqrt

L = [30, 40, 30, 30]

s = 0

for e in L:
    s += e
prom = s / len(L)

d = 0

for e in L:
    d += (e - prom)*(e - prom)
sd = sqrt(d / (len(L)-1))

print(sd)
