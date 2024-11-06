import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor a cero")
		n = int(input(msg))
	return n

def generar_vectores(n):
	dias = []
	desc = []
	mont = []
	descripciones = ["Viaje tranquilo", "Viaje complicado", "Viaje divertido"]
	for _  in range(n):
		dia = random.randint(1, 31)
		descripcion = random.choice(descripciones)
		monto = random.randint(1000, 30000)
		dias.append(dia)
		desc.append(descripcion)
		mont.append(monto)
	return dias, desc, mont

def menu():
	print("**********************MENU DE OPCIONES**********************")
	print("1) Monto promedio del mes")
	print("2) Mostrar envios realizados por importe")
	print("3) Dia del mes con mayor cantidad de transportes")
	print("0) ~ Salir ~")
	print("************************************************************")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 or opc < 0:
		print("Error. El valor ingresado no se encuentra entre las opciones")
		opc = int(input("Ingrese una opcion: "))
	return opc

def promedio_mensual(montos):
	acum = 0
	for monto in montos:
		acum += monto
	prom = acum // len(montos)
	print(f"El promedio mensual es de ${prom}")

def listado_envios(montos, dias, descripciones):
	listado = []
	for i in range(len(montos)):
		listado.append((montos[i], dias[i], descripciones[i]))
	listado.sort(reverse=True)
	for monto, dia, descripcion in listado:
		print(f"El monto es de ${monto}")
		print(f"En el dia {dia}")
		print(f"Con la descripcion {descripcion}")
		print("---------------------------------")
	
def dia_mayor_traslados(dias):
	contador = [0] * 31
	for dia in dias:
		contador[dia-1] += 1
	mayor = [0, 0]
	for i in range(len(contador)):
		if contador[i] > mayor[0]:
			mayor[0] = contador[i]
			mayor[1] = i+1
	print(f"El dia con mas traslados fue {mayor[1]} con {mayor[0]} traslados")
	
	
def principal():
	n = validar("Ingrese cantidad de transportes a generar: ")
	dias, descripciones, montos = generar_vectores(n)
	print("Datos cargados !!!")
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			promedio_mensual(montos)
		elif opc == 2:
			listado_envios(montos, dias, descripciones)
		elif opc == 3:
			dia_mayor_traslados(dias)
	print("Gracias por usar el programa! ")


if __name__ == "__main__":
	principal()
