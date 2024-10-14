def mayorMenor(a, b, c):
	mayor = max(a, b, c)
	menor = min(a, b, c)
	if a != mayor and a != menor:
		medio = a
	elif b != mayor and b != menor:
		medio = b
	else:
		medio = c
	
	if menor == mayor % medio or menor == medio % mayor:
		print(f"{menor} es el resto de los dos primeros!")
	
	print(f"El mayor es: {mayor}")
	print(f"El medio es: {medio}")
	print(f"El menor es: {menor}")
