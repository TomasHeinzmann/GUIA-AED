import random
def validar_n():
	n = int(input("Ingrese cantidad de elementos del arreglo: "))
	while n <= 0:
		print("Error. El arreglo no puede tener menos de 0 elementos")
		n = int(input("Ingrese cantidad de elementos del arreglo: "))
	return n
	
def generar_arreglo(n):
	v = []
	for _ in range(n):
		randNum = random.randint(1, 100)
		v.append(randNum)
	return v

def ordenar_arreglo(v):
	n = len(v)
	for i in range(n-1):
		ordenado = True
		for j in range(n - i - 1):
			if v[j] > v[j+1]:
				ordenado = False
				v[j], v[j+1] = v[j+1], v[j]
		if ordenado:
			break

def encontrar_x(v):
	x = int(input("Ingrese valor a buscar: "))
	if x in v:
		valores_impares = 0
		for nums in v:
			if nums % 2 != 0 and nums > x:
				valores_impares += 1
		print(f"Se encontraron {valores_impares} valores que cumplen la condicion")
	else:
		print("No se encontro ese elemento en el arreglo")

def principal():
	n = validar_n()
	v = generar_arreglo(n)
	ordenar_arreglo(v)
	print(v)
	encontrar_x(v)
	
	
if __name__ == "__main__":
	principal()
