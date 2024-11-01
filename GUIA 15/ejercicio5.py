import random

def validar_n():
	n = int(input("Ingrese cantidad de elementos del arreglo: "))
	while n <= 0:
		print("Error. La cantidad de elementos no puede ser igual o menor a 0")
		n = int(input("Ingrese cantidad de elementos del arreglo: "))
	return n

def cargar_vector(n):
	v = []
	for i in range(n):
		randNum = random.randint(1, 9)
		v.append(randNum)
	return v

def promedio_vector(v):
	largo = len(v); acumulador = 0
	for num in v:
		acumulador += num
	prom = acumulador / largo
	return prom

def mayor_prom(v, prom):
	mayores = 0
	for num in v:
		if num > prom:
			mayores += 1
	return mayores

def principal():
	n = validar_n()
	v = cargar_vector(n)
	prom = promedio_vector(v)
	mayores = mayor_prom(v, prom)
	print(f"Valor promedio de los numeros del arreglo: {prom}")
	print(f"Cantidad de numeros mayores al promedio: {mayores}")

if __name__ == "__main__":
	principal()
