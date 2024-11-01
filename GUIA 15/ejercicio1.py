import random


def menu():
	print("-----------------MENU DE OPCIONES - PLUVIOMETRO-----------------")
	print("1) Determinar promedio anual del pais")
	print("2) Determinar promedio de lluvias de un determinado trimestre")
	print("3) Determinar el mes mas seco del año")
	print("4) Determinar meses en los que llovio mas que el promedio anual")
	print("0) ~ Salir ~")
	opc = int(input("Ingrese una opcion: "))
	while opc > 4 and opc < 0:
		print("Error. El valor ingresado no es valido")
		opc = int(input("Ingrese una opcion: "))
	return opc

def punto1(lluvias):
	acumulador = 0
	for lluvia in lluvias:
		acumulador += lluvia
	return acumulador / 12

def punto2(lluvias):
	mes1 = int(input("Ingrese desde que numero de mes medir el trimestre: "))
	mes2 = int(input("Ingrese hasta que numero de mes medir el trimestre: "))
	diferencia = mes2 - mes1
	while not (mes2 > diferencia > mes1):
		diferencia += 1
	promedio_trimestre = (lluvias[mes1 - 1] + lluvias[diferencia - 1] + lluvias[mes2 - 1]) / 3
	return promedio_trimestre
	
def punto3(lluvias):
	menor = 1000
	for index, lluvia in enumerate(lluvias):
		if lluvia < menor:
			menor = index + 1
	return menor

def punto4(lluvias, promedio_anual):
	mayor_promedio = []
	for index, lluvia in enumerate(lluvias):
		if lluvia > promedio_anual:
			mayor_promedio.append(index + 1)
	if mayor_promedio:
		print("Los meses con lluvia mayor al promedio son: ")
		for lluvia in mayor_promedio:
			print(lluvia)
	else:
		print("No hubieron lluvias mayores al promedio")

def pluviometro():
	lluvias = []
	for i in range(12):
		lluvia = random.randint(1, 35)
		lluvias.append(lluvia)
	opc = -1
	flag_opc_1 = False
	while opc != 0:
		opc = menu()
		if opc == 1:
			promedio_anual = punto1(lluvias)
			flag_opc_1 = True
			print(f"El promedio anual del pais es {promedio_anual}")
		elif opc == 2:
			promedio_trimestre = punto2()
			print(f"El promedio de lluvia en el trimestre analizado es: {promedio_trimestre}")
		elif opc == 3:
			menor = punto3(lluvias)
			print(f"El menor mas seco del año fue {menor}")
		elif opc == 4:
			if 	flag_opc_1:
				punto4(lluvias, promedio_anual)
			else:
				print("Error, pase por la opcion 1 para calcular el promedio anual para este analisis")	
	print("Gracias por usar el programa!")
			


if __name__ == "__main__":
	pluviometro()
