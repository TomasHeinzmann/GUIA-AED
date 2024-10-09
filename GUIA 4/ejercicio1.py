def generadorMail ():
	nombre = input("Ingrese su nombre: ").lower()
	apellido = input("Ingrese su apellido: ").lower()
	dominio = input("Ingrese el dominio: ")
	
	if nombre[0] == apellido[0]:
		print(f"Mail generado: {nombre}.{apellido}@{dominio}")
	else:
		print(f"Mail generado: {nombre[0]}{apellido}@{dominio}")
		
generadorMail()
