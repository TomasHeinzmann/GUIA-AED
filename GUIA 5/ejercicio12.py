def notasAlumnos():
	parcial1 = int(input("Ingrese nota del primer parcial: "))
	parcial2 = int(input("Ingrese nota del segundo parcial: "))
	practico = int(input("Ingrese nota del practico: "))
	prom = (parcial1 + parcial2 + practico) / 3
	if round(prom, 2) < 4:
		print("El alumno esta libre!")
	elif 8 >= round(prom, 2) >= 4:
		print("El alumno esta regular!")
	elif round(prom, 2) > 8:
		print("El alumno esta promocionado!")
		
