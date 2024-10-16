def polinomio ():
	a = float(input("Ingrese valor de 'a' : "))
	b = float(input("Ingrese valor de 'b' : "))
	c = float(input("Ingrese valor de 'c' : "))
	
	disc = b ** 2 - 4 * a * c
	
	if disc < 0:
		res1 = (- b + (disc) ** 0.5) / (2 * a)
		res2 = (- b - (disc) ** 0.5) / (2 * a)
		print("Da como resultado numeros complejos")
	elif disc == 0:
		res1 = (- b + (disc) ** 0.5) / (2 * a)
		print(res1)
		res2 = a * (res1 ** 2) + b * res1 * c
		print(f"Existe una solucion, el resultado es: {res2}")
	elif disc > 0:
		res1 = (- b + (disc) ** 0.5) / (2 * a)
		res2 = (- b - (disc) ** 0.5) / (2 * a)
		print(f"Resultado de la primer raiz: {res1}")
		print(f"Resultado de la segunda raiz: {res2}")
	

