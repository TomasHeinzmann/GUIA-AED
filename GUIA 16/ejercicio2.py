import random


def validar_n(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor no puede ser menor o igual a cero")
		n = int(input(msg))
	return n

def generar_vector(n):
	v = []
	for i in range(n):
		randNum = random.randint(1, 100000)
		v.append(randNum)
	return v

def ordenar_vector(v):
	n = len(v)
	for i in range(n-1):
		ordenado = True
		for j in range(n-i-1):
			if v[j] > v[j+1]:
				ordenado = False
				v[j], v[j+1] = v[j+1], v[j]
		if ordenado:
			break

def buscar_alumno(v, x):
	encontrado = True
	for legajo in v:
		if legajo == x:
			print("Alumno encontrado!")
			print(legajo)
			break
		else:
			encontrado = False
	if not encontrado:
		print("No se encontro el legajo")
	

def principal():
	n = validar_n("Ingrese cantidad de legajos a crear: ")
	v = generar_vector(n)
	ordenar_vector(v)
	print(v)
	x = validar_n("Ingrese legajo a buscar: ")
	buscar_alumno(v, x)

if __name__ == "__main__":
	principal()
