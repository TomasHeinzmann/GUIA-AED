def tresCalculo():
	val1 = float(input("Ingrese el primer valor: "))
	val2 = float(input("Ingrese el segundo valor: "))
	val3 = float(input("Ingrese el tercer valor: "))
	
	mayVal = max(val1, val2, val3)
	minVal = min(val1, val2, val3)
	
	if val1 != mayVal and  val1 != minVal:
		midVal = val1
	elif val2 != mayVal and  val2 != minVal:
		midVal = val2
	else:
		midVal = val3
	
	sumVal = midVal + minVal
	
	if val1 % 5 == 0 or val1 % 5 == 0 or val3 % 5 == 0:
		print("Alguno de los valores es multiplo de 5")
		
	if val1 % 2 != 0 and val1 % 2 != 0 and val3 % 2 != 0:
		print("Todos los valores son impares")
		
	if mayVal > sumVal:
		print("El mayor de ellos supera la suma de los otros dos")
