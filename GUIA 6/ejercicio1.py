def complejoCine():
	cantEspec = -1
	desc = -1
	recTotal = cantDesc = cantFunc = rec = 0
	while cantEspec != 0:
		cantEspec = int(input("Ingrese cantidad de espectadores: "))
		if cantEspec != 0: 
			desc = input("Descuento (S/N): ")
			if desc == "S":
				rec = cantEspec * 50
				recTotal += rec
				cantDesc += 1
				print(f"Funcion con descuento, total: ${rec}")
			elif desc == "N":
				rec = cantEspec * 75
				recTotal += rec
				print(f"Funcion sin descuento, total: ${rec}")
			cantFunc += 1
	print(f"Recaudacion total del complejo: ${recTotal}")
	porcentDesc = cantDesc * 100 / cantFunc
	print(f"Porcentaje de funciones con descuento: {round(porcentDesc)}%")

