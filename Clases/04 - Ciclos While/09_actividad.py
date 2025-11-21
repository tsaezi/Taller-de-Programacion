#imprime las potencias de 2 desde 0 hasta n
i = 0
suma = 0
sk= 1

while abs(sk)>=0.00005:
  sk = ((-1)**i)/(2*i + 1)
  suma = sk + suma
  i  = i + 1

print(4*suma)
    
    