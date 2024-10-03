def sumaCuadrados (a, b):
	resultado1 = a ** 2 + b ** 2
	resultado2 = (a ** 3 + b ** 3) / 2 
	return f"La suma de cuadrados es {resultado1} y el promedio de cubos es {resultado2}"
	
print(sumaCuadrados(2, 2))
