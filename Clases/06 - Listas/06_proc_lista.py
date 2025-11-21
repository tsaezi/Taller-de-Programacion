#Imprimir lista
L = [11, 3, 5, 7, 2]
print('L', L)

#Verificar un elemento
if 11 in L:
    print('si está en L') 
else:
    print('no')

#Sublista
L3 = L[2:5] # Elementos 2,3 y 4
    
print('L[2:5]', L3)

# Actualizar elemento
L[4] = 9999
print('L[4]=9999', L)

# Agregar elemento a listas
L.append(100) #modifica lista
print('L.append(100)', L)

# Concatenar lista
L2 = L + [19, 17, 13] # crea lista nueva
print('L+[19, 17, 13]', L2)

