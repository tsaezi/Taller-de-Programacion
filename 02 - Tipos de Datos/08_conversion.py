amigos = input('Cuantos amigos tienes en facebook? ')
comun = input('Cuantos amigos tienes en comun con tu mejor amigo? ')

num_amigos = int(amigos)
num_comun = int(comun)
porcentaje = num_comun/num_amigos*100
print('Wow, tienes', porcentaje, '% de amigos en común con tu mejor amigo!')

print('tipo variable amigos:', type(amigos))
print('tipo variable num_amigos:', type(num_amigos))