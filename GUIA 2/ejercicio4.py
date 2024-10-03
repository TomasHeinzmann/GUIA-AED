def polinomioSegundoGrado(a, b, c, x):
	resultado1 = a * x ** 2 + b * x + c
	positivo = (-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 
	negativo = (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 
	print(f"resultado del polinomio en x: {resultado1}")
	print(f"raiz 1: {positivo}. raiz 2: {negativo}")
