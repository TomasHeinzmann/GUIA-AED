import random

def validar_n():
	n = int(input("Ingrese cantidad de elementos del vector: "))
	while n <= 0:
		print("Error. El vector no puede tener menos de 0 elementos")
		n = int(input("Ingrese cantidad de elementos del vector: "))
	return n

def generar_arreglo(n):
	v = []
	for i in range(n):
		randNum = random.randint(1, 9)
		v.append(randNum)
	return v

def arreglo_primos(v):
	v_primos = []
	for num in v:
		if num % 1 == 0 and num % num == 0 and not (num % 2 == 0) and not (num % 3 == 0):
			v_primos.append(num)
	return v_primos

def promedio_primos(v):
	cant_num = len(v); acumulador = 0
	for num in v:
		acumulador += num
	prom = acumulador / cant_num
	return prom

def buscar_numeros_primos():
	n = validar_n()
	v = generar_arreglo(n)
	v_primos = arreglo_primos(v)
	prom = promedio_primos(v_primos)
	print(f"Arreglo de numeros primos: {v_primos}")
	print(f"Promedio de numeros generados en el punto anterior: {round(prom, 2)}")
	
if __name__ == "__main__":
	buscar_numeros_primos()
