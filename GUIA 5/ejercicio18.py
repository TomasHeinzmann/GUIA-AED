def imc ():
	met = float(input("Ingrese su altura en metros: "))
	pes = float(input("Ingrese su peso en kilogramos: "))
	
	res = pes / (met ** 2)
	
	if res <= 16:
		print("Necesita asistencia de un médico, los riesgos para su salud son muy altos")
	elif res <= 17:
		print("Usted tiene infrapeso, aliméntese más")
	elif res <= 18:
		print("Usted tiene bajo peso, aliméntese mejor")
	elif 26 >= res > 18:
		print("Usted tiene un peso saludable, continúe así!")
	elif 30 > res >= 26:
		print("Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios")
	elif 35 >= res >= 30:
		print("Tiene obesidad de grado II, necesita el apoyo de un plan nutricional")
	elif 40 >= res > 35:
		print("Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud")
	else:
		print("Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico a la brevedad")

