import random

def validar(msg):
	n = int(input(msg))
	while n < 0: 
		print("Error. El valor ingresado no puede ser menor a 0")
		n = int(input(msg))
	return n

def menu():
	print("------------------------MENU DE OPCIONES------------------------")
	print("1) Obtener el promedio de los números de dos numeros")
	print("2) Obtener el menor número impar del lote")
	print("3) Imprimir todos los números múltiplos de un numero")
	print("0) ~ Salir ~")
	print("----------------------------------------------------------------")
	opc = validar("Ingrese una opcion: ")
	while opc > 3:
		print("Error. El valor ingresado no esta entre las opciones")
		opc = validar("Ingrese una opcion: ")
	return opc

def generar_arreglo():
	v = []
	for i in range(100):
		randNum = random.randint(1, 100000)
		v.append(randNum)
	return v

def promdio_entre_valores(val1, val2, v):
	cont, acum = 0, 0
	for valor in v:
		if val1 <= valor <= val2:
			cont += 1
			acum += valor
	if cont != 0:
		prom = acum / cont
	else:
		prom = 0
	return prom 

def obtener_menor_impar(v):
	menor = None
	for valor in v:
		if menor == None and valor % 2 != 0:
			menor = valor
		elif valor < menor and valor % 2 != 0:
			menor = valor
	return valor
	
def obtener_multiplos(x, v):
	multiplos = ""
	for valor in v:
		if valor % x == 0:
			multiplos += str(valor)
			multiplos += ", "
	return multiplos
		
	
def principal():
	opc = -1
	v = generar_arreglo()
	while opc != 0:
		opc = menu()
		if opc == 1:
			val1 = validar("Ingrese menor valor (desde): ")
			val2 = validar("Ingrese mayor valor (hasta): ")
			while val1 > val2:
				print("Error. El menor valor no puede ser mayor que el mayor valor")
				val1 = validar("Ingrese menor valor (desde): ")
				val2 = validar("Ingrese mayor valor (hasta): ")
			prom = promdio_entre_valores(val1, val2, v)
			print(f"El promedio entre los valores ingresados: {prom}")
		elif opc == 2:
			menor = obtener_menor_impar(v)
			print(f"Menor numero impar del lote: {menor}")
		elif opc == 3:
			x = validar("Ingrese el valor del que buscar los multiplos: ")
			multiplos = obtener_multiplos(x, v)
			print(multiplos)
	print("Gracias por usar el programa!")
if __name__ == "__main__":
	principal()
