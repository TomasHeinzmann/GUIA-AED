import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado no puede ser menor o igual a cero")
		n = int(input(msg))
	return n

def generar_vectores(n):
	desc = []
	descripciones = ["Modelo A", "Modelo B", "Modelo C", "Modelo D"]
	tipo = []
	mont = []
	for _ in range(n):
		eleccion1 = random.choice(descripciones)
		desc.append(eleccion1)
		eleccion2 = random.randint(0, 9)
		tipo.append(eleccion2)
		eleccion3 = random.randint(1000, 100000)
		mont.append(eleccion3)
	return desc, tipo, mont

def menu():
	print("---------------------------------------------MENU DE OPCIONES---------------------------------------------")
	print("1) Mostrar datos cargados")
	print("2) Determinar monto total facturado")
	print("3) Mostrar un listado ordenado alfabéticamente, de las ventas de los insumos del tipo x")
	print("4) Ventas de cada tipo de insumo")
	print("0) ~ Salir ~")
	print("-----------------------------------------------------------------------------------------------------------")
	opc = int(input("Ingrese una opcion: "))
	while opc > 4 or opc < 0:
		print("Error. La opcion ingresada no es valida, intente de nuevo")
		opc = int(input("Ingrese una opcion: "))
	return opc
	
def mostrar_datos(desc, tipo, montos):
	for i in range(len(desc)):
		print(f"Descripción: {desc[i]}")	
		print(f"Tipo: {tipo[i]}")
		print(f"Monto: {montos[i]}")
		print("-----------------------")

def monto_total(montos):
	total = 0
	for monto in montos:
		total += monto
	return total

def ventas_por_tipo(tipos, montos, descripciones, tipo_buscado):
    ventas_tipo = []
    for i in range(len(tipos)):
        if tipos[i] == tipo_buscado:
            ventas_tipo.append((descripciones[i], montos[i]))
    ventas_tipo.sort()
    for descripcion, monto in ventas_tipo:
        print(f"Descripción: {descripcion}, Monto: {monto}")

def contador_de_ventas_por_tipo(tipos):
	contador = [0] * 10
	for tipo in tipos:
		contador[tipo - 1] += 1
	for i in range(len(contador)):
		print(f"Las ventas de tipo {i + 1} son {contador[i]}")
	

def principal():
	n = validar("Ingrese cantidad de ventas a generar: ")
	descripciones, tipos, montos = generar_vectores(n)
	opc = -1
	while opc != 0:
		opc = menu()
		if opc == 1:
			mostrar_datos(descripciones, tipos, montos)
		elif opc == 2:
			total = monto_total(montos)
			print(f"Monto total facturado ${total}")
		elif opc == 3:
			tipo_ingresado = int(input("Ingrese tipo de venta a buscar: "))
			ventas_por_tipo(tipos, montos, descripciones, tipo_ingresado)
		elif opc == 4:
			contador_de_ventas_por_tipo(tipos)
	print("Gracias por usar el programa!")
			
			
			

if __name__ == "__main__":
	principal()
