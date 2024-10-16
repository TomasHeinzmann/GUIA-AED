def senado():
	fav = int(input("Ingrese cantidad de votos a favor: "))
	con = int(input("Ingrese cantidad de votos en contra: "))
	abt = int(input("Ingrese cantidad de abstensiones: "))
	
	total = fav + con + abt
	ausen = 72 - total
	
	porcenFav = fav * 100 / 72
	porcenCon = con * 100 / 72
	porcenConAbt = (con + abt) * 100 / 72
	if porcenFav > porcenConAbt:
		print(f"Se aprobo por mayoria absoluta, con un {porcenFav}% a favor")
	elif porcenFav > porcenCon:
		print(f"Se aprobo por mayoria simple, con un {porcenFav}% a favor")
	else:
		print(f"No se aprobo, con un {porcenCon}% en contra")
	if ausen > 0:
		print(f"{ausen} senadores estaban ausentes")
	else:
		print("Todos los senadores estaban presentes")

senado()
