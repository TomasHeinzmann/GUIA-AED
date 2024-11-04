import random

def generar_jurado():
	v = []
	for i in range(7):
		randNum = random.randint(-1, 10)
		v.append(randNum)
	return v

def buscar_mejores_puntajes(v):
	copia_v = v.copy()
	mejores = []
	for i in range(3):
		mejor = max(copia_v)
		copia_v.remove(mejor)
		mejores.append(mejor)
	return mejores

def validar_n(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado no puede ser menor o igual a cero")
		n = int(input(msg))
	return n

def buscar_mayores_que(v, x):
	encontrado = False
	for i in range(len(v)):
		if v[i] > x:
			print(v[i])
			encontrado = True
	if not encontrado:
		print("No hay notas mayores a la ingresada")
		
def diferencia_menor_mayor(v):
	menor = 11
	mayor = -2
	for i in range(len(v)):
		if v[i] > mayor:
			mayor = v[i]
		elif v[i] < menor:
			menor = v[i]
	dif = mayor - menor
	return dif

def contar_puntaje(v):
	acum = 0
	for i in range(len(v)):
		if i != 0 and i != 6:
			acum += v[i]
		elif i == 0:
			extr1 = v[i]
		elif i == 6:
			extr2 = v[i]
	final = acum + extr1 + extr2
	if final >= 20:
		prom = acum / 5
		print(f"Los bailarines tuvieron un puntaje de {prom} !!!")
	else:
		print("Los bailarines estan descalificados!")
	
	

def principal():
	jurado = generar_jurado()
	mejores = buscar_mejores_puntajes(jurado)
	x = validar_n("Mostrar puntuaciones mayores a esta: ")
	buscar_mayores_que(jurado, x)
	dif = diferencia_menor_mayor(jurado)
	print(f"La diferencia entre el mayor y menor puntaje es: {dif}")
	contar_puntaje(jurado)
	print(jurado)
	print(mejores)

if __name__ == "__main__":
	principal()
