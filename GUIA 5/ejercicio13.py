def definirCuadrante():
	x = int(input("Ingrese el valor de x: "))
	y = int(input("Ingrese el valor de y: "))
	if x > 0 and y > 0:
		print("El punto esta en el primer cuadrante")
	elif x < 0 and y > 0:
		print("El punto esta en el segundo cuadrante")
	elif x < 0 and y < 0:
		print("El punto esta en el tercer cuadrante")
	elif x > 0 and y < 0:
		print("El punto esta en el cuarto cuadrante")
	else:
		print("El punto esta en el origen del sistema")
