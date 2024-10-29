import random

def validar_token():
	token = input("Ingrese su token: ")
	mayus = "QWERTYUIOPÑLKJHGFDSAMNBVCXZ"
	cant_mayus = 0; cant_nums = 0; long_token = 0; posicion_numeral = 0
	token_valido = False
	for caracter in token:
		long_token += 1
		if caracter in mayus:
			cant_mayus += 1
		elif caracter.isnumeric():
			cant_nums += 1
		elif caracter == "#":
			posicion_numeral = long_token
	if cant_mayus == 2 and cant_nums >= 2 and long_token // 2 < posicion_numeral:
		token_valido = True
	return token_valido

def operaciones_bancarias():
	n = int(input("Ingrese cantidad de operaciones bancarias a procesar: "))
	operaciones = []; tipos = ["empresa", "particular"]
	divisas = ["pesos", "dolares"]
	while n <= 0:
		print("Error. No se puede ingresar numeros menores o iguales a cero")
		n = int(input("Ingrese cantidad de operaciones bancarias a procesar: "))
	for i in range(n):
		tipo = random.choice(tipos)
		monto = random.randint(1, 1000000)
		divisa = random.choice(divisas)
		operacion = [tipo, monto, divisa]
		operaciones.append(operacion)
	return operaciones

def menu():
	print("--------------------MENU DE OPERACIONES--------------------")
	print("1) Cantidad operaciones que se llevaron a cabo")
	print("2) Porcentaje de operaciones en dólares")
	print("3) Monto total operado en pesos por particulares")
	print("4) Monto promedio operado en pesos por las empresas")
	print("0) ~ Salir ~")
	opc = int(input("Ingrese una opcion: "))
	while 4 < opc > 0:
		print("Error. El valor se sale de los parametros")
		opc = int(input("Ingrese una opcion: "))
	return opc
	

def porcentaje_operaciones_dolares(operaciones):
	cant_operaciones = len(operaciones)
	operacion_dolares = 0
	for operacion in operaciones:
		if operacion[2] == "dolares":
			operacion_dolares += 1
	porcent = operacion_dolares * 100 // cant_operaciones
	return porcent

def monto_total_particular_pesos(operaciones):
	monto_total = 0
	for operacion in operaciones:
		if operacion[0] == "particular" and operacion[2] == "pesos":
			monto_total += operacion[1]
	return monto_total

def monto_medio_empresas_pesos(operaciones):
	monto = 0; cant = 0
	for operacion in operaciones:
		if operacion[0] == "empresa" and operacion[2] == "pesos":
			cant += 1
			monto += operacion[1]
	prom = monto // cant
	return prom
	
def entidad_bancaria():
	token_valido = validar_token()
	if token_valido:
		print("Token valido")
		operaciones = operaciones_bancarias()
		opc = -1
		while opc != 0:
			opc = menu()
			if opc == 1:
				cant_operaciones = len(operaciones)
				print(f"Numero de operaciones: {cant_operaciones}")
			elif opc == 2:
				porcent = porcentaje_operaciones_dolares(operaciones)
				print(f"Porcentaje de operaciones en dolares: {porcent}%")
			elif opc == 3:
				monto = monto_total_particular_pesos(operaciones)
				print(f"Monto total de operaciones de particulares en pesos: ${monto}")
			elif opc == 4:
				prom = monto_medio_empresas_pesos(operaciones)
				print(f"Monto promedio de operaciones de empresas en pesos: ${prom}")
		print("Gracias por usar el programa! ")
		
	else:
		print("El token no es valido")

if __name__ == "__main__":
	entidad_bancaria()
