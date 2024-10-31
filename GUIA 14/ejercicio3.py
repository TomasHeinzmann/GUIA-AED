

def sumar_pares(n):
	if n <= 0:
		return 0
	elif n % 2 == 0:
		return n + sumar_pares(n - 2)
	else:
		sumar_pares(n - 1)

def pedir_numero():
	n = int(input("Ingrese un numero mayor o igual a cero: "))
	if n < 0:
		print("Error. El numero debe ser mayor a cero")
		return pedir_numero()
	return n

n = pedir_numero()

print(f"La suma de numeros pares desde {n} es {sumar_pares(n)}")
