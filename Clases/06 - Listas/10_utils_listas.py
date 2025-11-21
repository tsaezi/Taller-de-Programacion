# lista con valores desde teclado
L = [] #lista vací­a
N=3
for i in range(N):
    v = int(input("Ingrese elemento" + "\n"))
    L.append(v)


print('-----------------------------------')
# imprimir elementos en lista
print('Imprimir elementos en lista L:', '\n')
for elem in L:
    print(elem)

print('-----------------------------------')
# imprimir elementos en lista (otra forma)
print('Imprimir elementos en lista L:', '\n')
for i in range(N):
    print(L[i])

print('-----------------------------------')    
# encontrar el máximo
print('Maximo', '\n')
maxi = L[0]
for elem in L:
    if elem > maxi:
        maxi = elem
print("El maximo es:", maxi)

print('-----------------------------------')
# encontrar el mínimo
print('Minimo', '\n')
mini = L[0] 
for elem in L:
    if elem < mini:
        mini = elem
print("El minimo es:",mini)
print('-----------------------------------')
# promedio
suma = 0.0
for elem in L:
    suma = suma + elem
prom = suma/N
print('El promedio es:', prom)

print('-----------------------------------')
# copiar lista
L2 = []
for elem in L:
    L2.append(elem)

# invertir elementos de la lista
for i in range(N):
    temp = L[i]
    L[i] = L[N-i-1]
    L[N-i-1] = temp
    
print('L:',L)

# insertar elemento al final
L.append(33)
print('L:', L)