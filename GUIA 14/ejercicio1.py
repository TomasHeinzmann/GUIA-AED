
def factorial_iteracion(n):
	resultado = 1
	for i in range(n):
		resultado *= i + 1
	print(f"El factorial de {n} es {resultado}")
	
def factorial_recursiva(n):
	if n == 1:
		return n
	else:
		return n * factorial_recursiva(n - 1)
	
def fibonacci_recursivo(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursivo(n-1) + fibonacci_recursivo(n-2)

def fibonacci_iteracion(n):
	inicio, siguiente = 0, 1
	if n == 0:
		return n
	elif n == 1:
		return n
	for i in range(2, n	+ 1):
			inicio, siguiente = siguiente, inicio + siguiente
	return siguiente

def secuencia_ascendente(n):
	if n > 1:
		secuencia_ascendente(n - 1)
	print(n, end=" ")

def secuencia_descendente(n):
	print(n, end=" ")
	if n > 1:
		secuencia_descendente(n - 1)

if __name__ == "__main__":
	n = int(input("Ingrese un numero: "))
	factorial_iteracion(n)
	print(factorial_recursiva(n))
	print(fibonacci_recursivo(n))
	print(fibonacci_iteracion(n))
	print(secuencia_ascendente(n))
	print(secuencia_descendente(n))
