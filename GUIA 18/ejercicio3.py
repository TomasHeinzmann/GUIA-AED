import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor a 0")
		n = int(input(msg))
	return n

def generar_multas(n):
	codigos = []
	categorias = []
	for i in range(n):
		codigo = random.randint(1, 20)
		final = codigo % 10
		if final == 1 or final == 6:
			tipo = 1
		elif final == 2 or final == 7:
			tipo = 2
		elif final == 3 or final == 8:
			tipo = 3
		elif final == 4 or final == 9:
			tipo = 4
		elif final == 5 or final == 0:
			tipo = 0
		codigos.append(codigo)
		categorias.append(tipo)
	return codigos, categorias

def menu():
	print("****************************MENU DE OPCIONES****************************")
	print("1) Mostrar los importes totales facturados por tipo de infraccion")
	print("2) Codigo de infraccion que mas aparecio en las multas")
	print("3) Importe total facturado durante el fin de semana")
	print("0) ~ Salir ~")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 or opc < 0:
		print("Error. La opcion ingresada no se encuentra entre las disponibles")
		opc = int(input("Ingrese una opcion: "))
	return opc

def importes_por_categoria(categorias):
	importes = [0] * len(categorias)
	monto_base = 1000
	for i in range(len(categorias)):
		if categorias[i] == 0:
			importes[i] += monto_base
		else:
			importes[i] += monto_base * categorias[i] + monto_base
	return importes

def codigo_que_mas_aparece(codigos):
	contador = [0] * 20
	for codigo in codigos:
		contador[codigo-1] += 1
	mayor = [0, 0]
	for i in range(len(contador)):
		if contador[i] > mayor[0]:
			mayor[0] = contador[i]
			mayor[1] = i+1
	print(f"El codigo que mas veces aparecio es {mayor[1]}")
	print(f"Aparecio un total de {mayor[0]} veces")

def importe_total(importes):
	total = 0
	for importe in importes:
		total += importe
	print(f"El importe total durante el fin de semana fue ${total}")

def principal():
	n = validar("Ingrese cantidad de multas a generar: ")
	codigos, categorias = generar_multas(n)
	print("Datos cargados !!!")
	opc = -1
	importes = None
	while opc != 0:
		opc = menu()
		if opc == 1:
			importes = importes_por_categoria(categorias)
		elif opc == 2:
			codigo_que_mas_aparece(codigos)
		elif opc == 3:
			if importes == None:
				print("Error. Debe pasar por el primer punto primero")
			else:
				importe_total(importes)
	print("Gracias por usar el programa!")
			

if __name__ == "__main__":
	principal()
