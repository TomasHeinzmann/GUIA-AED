import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado debe ser mayor a cero")
		n = int(input(msg))
	return n

def generar_productos(n):
	codigos = []
	categorias = []
	importes = []
	for _ in range(n):
		codigo = random.randint(1, 80)
		categoria = random.randint(1, 10)
		importe = categoria * 1000 + 1000
		codigos.append(codigo)
		categorias.append(categoria)
		importes.append(importe)
	return codigos, categorias, importes  

def menu():
	print("****************MENU DE OPCIONES****************")
	print("1) Cargar productos")
	print("2) Mostrar costo de produccion de un producto")
	print("3) Costo total por categoria de producto")
	print("4) Categoria de productos mas fabricada")
	print("0) ~ Salir ~")
	print("************************************************")
	opc = int(input("Ingrese una opcion: "))
	while opc > 4 or opc < 0:
		print("Error. La opcion ingresada es incorrecta")
		opc = int(input("Ingrese una opcion: "))
	return opc

def mostrar_costo_produccion(x, codigos, importes):
	total_costos = 0
	for i in range(len(codigos)):
		if codigos[i] == x:
			total_costos += importes[i]
	print(f"El costo total de produccion fue ${total_costos}") 

def costo_total_por_categoria(categorias, importes):
	contador = [0] * 10
	for i in range(len(categorias)):
		contador[categorias[i]-1] += importes[i]
	contador.sort()
	for i in range(len(contador)):
		print(f"El costo de la categoria {i+1} es ${contador[i]}")

def categoria_mas_fabricada(categorias):
	contador = [0] * 10
	for categoria in categorias:
		contador[categoria - 1] += 1
	mayor_categoria = max(contador)
	index_mayor_categoria = contador.index(mayor_categoria) + 1
	print(f"La categoria mayor fabricada fue {mayor_categoria} con {index_mayor_categoria} productos fabricados")

def principal():
	opc = -1
	punto1 = False
	while opc != 0:
		opc = menu()
		if opc == 1:
			n = validar("Ingrese cantidad de productos: ")
			codigos, categorias, importes = generar_productos(n)
			punto1 = True
		elif not punto1 and opc != 0:
			print("Para acceder a las otras opciones, pase primero por el punto 1")
		elif punto1:
			if opc == 2:
				x = int(input("Ingrese codigo del producto: "))
				mostrar_costo_produccion(x, codigos, importes)
			elif opc == 3:
				costo_total_por_categoria(categorias, importes)
			elif opc == 4:
				categoria_mas_fabricada(categorias)
	print("Gracias por usar el programa!")
	

if __name__ == "__main__":
	principal()
