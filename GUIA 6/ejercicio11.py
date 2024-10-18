def discriminantes():
	opc = "S"
	cantPos = cantCer = cantNeg = 0
	while opc == "S":
		opc = input("Desea cargar discriminantes? (S/N): ")
		if opc == "S":
			a = int(input("Ingrese el valor de 'a': "))
			b = int(input("Ingrese el valor de 'b': "))
			c = int(input("Ingrese el valor de 'c': "))
			dis = b ** 2 - 4 * a * c
			if dis > 0:
				cantPos += 1
			elif dis == 0:
				cantCer += 1
			elif dis < 0:
				cantNeg += 1
		else:
			print("Gracias por usar el progama!")
	
	total = cantPos + cantNeg + cantCer
	porcentNeg = cantNeg * 100 / total
	
	print(f"Cantidad de discriminantes que dan dos raices reales: {cantPos}")
	print(f"Cantidad de discriminantes que da una raiz: {cantCer}")
	print(f"Cantidad de discriminantes que dan dos raices complejas: {cantNeg}")
	print(f"Las raices complejas representan un {porcentNeg}% del total de raices")

discriminantes()
