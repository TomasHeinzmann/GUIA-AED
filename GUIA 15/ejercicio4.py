import random

def validar_n():
	n = int(input("Ingrese cantidad de elementos del vector: "))
	while n <= 0:
		print("Error. El vector no puede tener cero o menos de cero elementos")
		n = int(input("Ingrese cantidad de elementos del vector: "))
	return n

def cargar_vectores(n):
	vector1 = []
	for _ in range(n):
		randNum = random.randint(1, 9)
		vector1.append(randNum)
	vector2 = []
	for _ in range(n):
		randNum = random.randint(1, 9)
		vector2.append(randNum)
	return vector1, vector2

def mayor_vector(v1, v2):
	vector3 = []
	for index, num in enumerate(v1):
		mayor = max(v1[index], v2[index])
		vector3.append(mayor)
	return vector3

if __name__ == "__main__":
	n = validar_n()
	vector1, vector2 = cargar_vectores(n)
	mayores_valores = mayor_vector(vector1, vector2)
	print(f"Mayores elementos de los compenentes homologos: {mayores_valores}")
