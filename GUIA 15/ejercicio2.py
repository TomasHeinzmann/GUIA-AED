import random


def ultimoPrimero():
	vector = []
	n = int(input("Ingrese cantidad de elementos del vector: "))
	while n < 0:
		print("Error, la cantidad no puede ser negativa")
		n = int(input("Ingrese cantidad de elementos del vector: "))
	
	for _ in range(n):
		randNum = random.randint(1, 9)
		ultimo = randNum
		vector.append(randNum)
	
	primer_valor = vector[0]
	cant_ultimo = 0
	nuevo_vector = []
	for num in vector:
		if ultimo == num:
			cant_ultimo += 1
		if num < primer_valor:
			nuevo_vector.append(num)
	
	print(f"Veces que aparece el ultimo digito en el vector: {cant_ultimo}")
	print(f"Vector nuevo (con valores mayores que el primer valor del vector original): {nuevo_vector}")

if __name__ == "__main__":
	ultimoPrimero()
