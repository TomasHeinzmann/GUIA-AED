
n = int(input("Ingrese un numero: "))

def sumar_digitos(n):
	if n < 10:
		return n
	else:
		return (n % 10) + sumar_digitos(n // 10)

print(sumar_digitos(n))
