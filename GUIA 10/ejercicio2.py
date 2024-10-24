
def secuenciaNumerica():
	num = -1
	divCuatro = 0
	mayImpar = 0
	cantNums = 0
	cantPrimero = 1
	antNum = 0
	contSec = 0
	flagTres = False
	while num != 0:
		num = int(input("Ingrese numero de la secuencia: "))
		if num != 0:
			cantNums += 1
			if num % 4 == 0:
				divCuatro += 1
			else:
				pass
			if num % 2 != 0 and num > mayImpar:
				mayImpar = num
			else:
				pass
			if cantNums == 1:
				primerNumero = num
			elif num == primerNumero:
				cantPrimero += 1
			else:
				pass
			if antNum == 1 and num == 2:
				flagTres = True
			else:
				pass
			if flagTres:
				contSec += 1
				flagTres = False
			else:
				pass
			antNum = num
		else:
			pass
	print(f"Numeros divisibles por 4: {divCuatro}")
	print(f"Mayor impar ingresado: {mayImpar}")
	print(f"Veces que aparecio el primero: {cantPrimero}")
	print(f"Veces que aparecio la secuencia (1, 2, 3): {contSec}")

secuenciaNumerica()
