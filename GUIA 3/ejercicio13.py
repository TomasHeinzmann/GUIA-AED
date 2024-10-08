def trianguloCalculo(cateto1, cateto2):
	hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5
	ladoMayor = max(hipotenusa, cateto1, cateto2)
	ladoMenor = min(hipotenusa, cateto1, cateto2)
	print(f"Valor de la hipotenusa: {round(hipotenusa, 2)}")
	print(f"Lado de mayor valor: {round(ladoMayor, 2)}")
	print(f"Lado de menor valor: {round(ladoMenor, 2)}")

trianguloCalculo(10, 15)
