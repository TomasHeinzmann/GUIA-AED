import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor a 0")
		n = int(input(msg))
	return n
	
def generar_vectores(n):
	v1, v2 = [], []
	for i in range(n):
		tipo = random.randint(0, 3)
		cant = random.randint(1, 30)
		v1.append(tipo)
		v2.append(cant)
	return v1, v2

def contar_ventas(v1, v2):
	contador = [0] * 4
	for i in range(len(v1)):
		contador[v1[i]] += v2[i]
	return contador

def principal():
	n = validar("Ingrese cantidad de articulos a generar: ")
	v1, v2 = generar_vectores(n)
	print(v1)
	print(v2)
	contador = contar_ventas(v1, v2)
	print(contador)

if __name__ == "__main__":
	principal()
