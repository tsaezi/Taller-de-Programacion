from random import randrange

VALORES = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jota', 'Reina', 'Rey', 'As']
         
TRAJES = ['Picas', 'Diamantes', 'Treboles', 'Corazones']


valor = randrange(0, len(VALORES))

print('valor', valor)

traje = randrange(0, len(TRAJES))

print('traje',traje)

print(VALORES[valor],'de', TRAJES[traje])
