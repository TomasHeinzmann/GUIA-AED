def plazoFijo():
	plata = int(input("Ingrese cantidad de dinero para plazo fijo: "))
	plata = round(plata + plata * 0.023, 2)
	plataGastos = round(plata - 20, 2)
	print(f"Cantidad de dinero por plazo fijo {plata} menos gastos {plataGastos}")

