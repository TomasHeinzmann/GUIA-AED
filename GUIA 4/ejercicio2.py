def calculoNumeros (a, b, c):
	suma = a + b + c
	if suma > 10:
		suma //= 10
		print(suma)
	else:
		suma **= 3
		print(suma)
