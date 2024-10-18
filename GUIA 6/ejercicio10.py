def comisionVendedores():
	cat = ven = -1
	com1 = com2 = com3 = com4 = 0
	while cat != 0:
		cat = int(input("Ingrese categoria del vendedor: "))
		if cat != 0:
			ven = int(input("Ingrese total de la venta: "))
			if cat == 1:
				com1 += ven * 0.10
			elif cat == 2:
				com2 += ven * 0.25
			elif cat == 3:
				com3 += ven * 0.30
			elif cat == 4:
				com4 += ven * 0.40
			else:
				print("Gracias por usar el programa!")
	
	total = com1 + com2 + com3 + com4
	
	print(f"Total a pagar por primer categoria: {com1}")
	print(f"Total a pagar por segunda categoria: {com2}")
	print(f"Total a pagar por tercera categoria: {com3}")
	print(f"Total a pagar por cuarta categoria: {com4}")
	print(f"Total general: {total}")
