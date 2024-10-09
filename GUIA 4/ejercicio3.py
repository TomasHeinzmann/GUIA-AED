def jornalOperario():
	horario = None
	while horario != 1 and horario != 2:
		horario = int(input("Ingrese turno trabajado (1-Diurno, 2-Nocturno): "))
		if horario == 1:
			horas = int(input("Ingrese cantidad de horas trabajadas: "))
			horas *= 35.50
			print(f"El pago es de: ${horas}")
		elif horario == 2:
			horas = int(input("Ingrese cantidad de horas trabajadas: "))
			horas *= 40.60
			print(f"El pago es de: ${horas}")
		else:
			print("Error. El horario solo puede ser 1 o 2")
			
jornalOperario()
