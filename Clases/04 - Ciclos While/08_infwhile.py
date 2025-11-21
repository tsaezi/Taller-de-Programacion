# Un ciclo while que nunca termina!
x = 1
while True:
    print("Al infinito y más allá! Ya vamos en {:d}!".format(x))
    x=x+1
    if x ==100:
        break
