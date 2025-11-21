def fib(n):    #Escribe la serie Fibonacci hasta n
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        print(b)
	

def fib2(n):   #Devuelve la serie Fibonacci hasta n
    resultado = []
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        resultado.append(b)
    return resultado

fib(13)

print(fib2(13))
