def galeriaArte():
	obra1 = int(input("Ingrese año de creacion de la primer obra: "))
	obra2 = int(input("Ingrese año de creacion de la segunda obra: "))
	obra3 = int(input("Ingrese año de creacion de la tercer obra: "))
	
	if obra1 < 1901 and obra2 < 1901 and obra3 < 1901:
		print("Todas las obras son anteriores al siglo XX")
	else:
		print("Alguna de las obras es del siglo XX")
	
	fechaCreacion = int(input("Ingrese un posible año de creacion de alguna obra: "))
	if fechaCreacion == obra1 or fechaCreacion == obra2 or fechaCreacion == obra3:
		print("Alguna de las obras fue creada en el año ingresado")
	else: 
		print("Ninguna de las obras fue creada en el año ingresado")

	obraAntigua = min(obra1, obra2, obra3)
	obraNueva = max(obra1, obra2, obra3)
	diferencia = obraNueva - obraAntigua
	
	print(f"La diferencia de años entre la obra mas nueva y la mas antigua es de: {diferencia} años")
