notas = {'Diego'    : 4.1
        ,'Francisca': 5.5
        ,'Daniela'  : 6.8
        ,'Leo'      : 3.9}


#Imprimir llaves        
for llave in notas.keys():
    print(llave )
    
print('\n')
  
#Imprimir valores
for valor in notas.values():
    print(valor)
    
print('\n')
 
#Imprimir llaves y los valores
for llave, valor in notas.items():
    print(llave, valor)

print('\n')

print('notas:',notas)