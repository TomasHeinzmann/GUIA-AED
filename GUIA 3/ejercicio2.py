def diaMesAño ():
	fecha = input("Ingrese fecha en formato dd/mm/aaaa: ")
	dia = fecha[0] + fecha[1]
	mes = fecha[3] + fecha[4]
	año = fecha[6] + fecha[7] + fecha[8] + fecha[9]
	print(f"Dia: {dia}, Mes: {mes}, Año: {año}")

