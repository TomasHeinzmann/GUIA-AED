# 16 caracteres por numero de tarjeta
import random

def cargar_tarjetas_invalidas():
	ingreso = 1
	tarjetas = []
	invalida = False
	while ingreso != 2:
		ingreso = int(input("Desea cargar una tarjeta invalida ? (1-si, 2-no): "))
		if ingreso == 1:
			tarjeta = input("Ingrese numero de tarjeta: ")
			for caracter in tarjeta:
				invalida = False
				if not caracter.isnumeric():
					invalida = True
			if len(tarjeta) == 16 and not invalida:
				tarjetas.append(tarjeta)
			print("Tarjeta cargada!")
	print("Perfecto ! Las tarjetas invalidas ya se cargaron al sistema")
	return tarjetas

def generar_tarjetas():
	tarjetas = []
	for i in range(20):
		tarjeta = str(random.randint(1000000000000000, 9999999999999999))
		tarjetas.append(tarjeta)
	return tarjetas

def contador_rechazos(lista_invalidas, lista_tarjetas):
	contador = [0] * 9
	for tarjeta in lista_tarjetas:
		if tarjeta in lista_invalidas:
			primer_digito = int(tarjeta[0])
			contador[primer_digito - 1] += 1 
	mayores_rechazos = max(contador)
	index_mayores_rechazos = contador.index(mayores_rechazos) + 1
	for i in range(len(contador)):
		if contador[i] > 0:
			print(f"La marca correspondiente a {i + 1} tiene {contador[i]} rechazos")
	print(f"La marca con mas rechazos es {index_mayores_rechazos} con {mayores_rechazos} rechazos")

def principal():
	lista_tarjetas = generar_tarjetas()
	print(lista_tarjetas)
	lista_invalidas = cargar_tarjetas_invalidas()
	contador_rechazos(lista_invalidas, lista_tarjetas)

if __name__ == "__main__":
	principal()
