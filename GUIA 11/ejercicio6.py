def analizar_primer_linea(linea):
	fecha = ""
	if "CO" in linea:
		provincia = "Cordoba"
	elif "SF" in linea:
		provincia = "Santa Fe"
	elif "BA" in linea:
		provincia = "Buenos Aires"
	else:
		provincia = "Entre Rios"	
	for caracter in linea:
		if caracter == " " or caracter == "-" or caracter == "/":
			pass
		else:
			if caracter.isnumeric():
				fecha += caracter
	dia = fecha[0] + fecha[1]
	mes = fecha[2] + fecha[3]
	año = fecha[4] + fecha[5] + fecha[6] + fecha[7]
	print(f"Provincia: {provincia}")
	print(f"Fecha: {dia}/{mes}/{año}")
			


def leer_archivo():
	archivo = open("cobros.txt", "r")
	lineas = archivo.readlines()
	agua_gas_internet = 0; credito = 0; impuestos_tasas = 0
	suma_julio_agosto = 0; cantidad_punto_3 = 0; cant_vocales = 0
	total_cobros = 0; cantidad_menor_6 = 0
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"
	for i in range(len(lineas)):
		linea = lineas[i]
		if i != 0:
			total_cobros += 1
			# PUNTO 2 
			if linea[8] == "0":
				agua_gas_internet += 1
			elif linea[8] == "1":
				credito += 1
			elif linea[8] == "2":
				impuestos_tasas += 1
			# PUNTO 3
			if linea[4] == "0" and linea[5] == "0" and linea[8] == "0":
				cobro = float(linea[9:15])
				suma_julio_agosto += cobro
			elif linea[4] == "0" and linea[5] == "7" and linea[8] == "0":
				cobro = float(linea[9:15])
				suma_julio_agosto += cobro
			# PUNTO 4
			for caracter in linea:
				if caracter.isnumeric():
					caracterNum = int(caracter)
					if caracterNum % 2 != 0:
						cantidad_punto_3 += 1
						continue
				elif caracter == "K":
					cantidad_punto_3 += 1
				if caracter in vocales:
					cant_vocales += 1
				if cant_vocales > 2:
					cantidad_punto_3 += 1
			cant_vocales = 0
			# PUNTO 5
			if linea[27:].isnumeric():
				numero_local = int(linea[27:])
				if numero_local <= 6:
					cantidad_menor_6 += 1
		else:
			analizar_primer_linea(linea)
		
		if cantidad_menor_6 > 0:
			porcent = cantidad_menor_6 * 100 / total_cobros
		else:
			porcent = 0
	print(f"Cantidad de cobros por tipo de cobro: {agua_gas_internet} agua, gas o internet")
	print(f"Cantidad de cobros por tipo de cobro: {credito} cobro tarjetas credito")
	print(f"Cantidad de cobros por tipo de cobro: {impuestos_tasas} impuestos y tasas")
	print(f"Total cobrado por agua, gas o internet entre julio y agosto: {suma_julio_agosto}")
	print(f"Solo digitos impares y una K o dos vocales: {cantidad_punto_3}")
	print(f"Porcentaje de cobros a locales con numero menor o igual a 6: {round(porcent, 2)}%")


leer_archivo()
