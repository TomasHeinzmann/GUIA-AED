import random

def validar_n(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor que 0")
		n = int(input(msg))
	return n

def generar_muestras(n):
	v = []
	for i in range(n):
		temperatura = random.randint(5, 30)
		region = random.randint(1, 20)
		dia = random.randint(1, 31)
		muestra = [temperatura, region, dia]
		v.append(muestra)
	return v

def prom_muestras(v):
	acum = 0
	for muestra in v:
		acum += muestra[0]
	prom = acum / len(v)
	return prom

def buscar_por_region(region, v):
	muestras_region = []
	for muestra in v:
		if muestra[1] == region:
			muestras_region.append(muestra)
	if muestras_region:
		n = len(muestras_region)
		for i in range(n):
			for j in range(n-i-1):
				if muestras_region[j][2] > muestras_region[j+1][2]:
					muestras_region[j], muestras_region[j+1] = muestras_region[j+1], muestras_region[j]
	return muestras_region

def buscar_mayores_temperaturas(temp, region, v):
	encontrado = False
	for muestra in v:
		if muestra[1] == region and muestra[0] > temp:
			encontrado = True
	if encontrado: 
		print("Hay temperaturas en esa region que superan a la ingresada!")
	else:
		print("No hay temperaturas que superen a la ingresada")

def muestras_por_region(v):
	muestras = [0] * 20
	for muestra in v:
		muestras[muestra[1]-1] += 1
	return muestras

def principal():
	n = validar_n("Ingrese cantidad de muestrar a generar: ")
	v = generar_muestras(n)
	prom = prom_muestras(v)
	print(v)
	region = validar_n("Ingrese region de la que se quiera buscar muestras: ")
	muestras_region = buscar_por_region(region, v)
	print(muestras_region)
	region = validar_n("Ingrese region con la que comparar temperaturas: ")
	temp = validar_n("Ingrese temperatura a superar: ")
	buscar_mayores_temperaturas(temp, region, v)
	muestras = muestras_por_region(v)
	print(muestras)
	print(f"Promedio de temperaturas: {prom}")

if __name__ == "__main__":
	principal()
