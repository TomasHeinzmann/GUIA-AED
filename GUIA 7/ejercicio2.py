def secImpares():
	num1 = int(input("Ingrese el primer numero (desde):"))
	num2 = int(input("Ingrese el segundo numero (hasta):"))
	listNums = []
	for num in range(num1, num2 + 1):
		if num % 2 != 0:
			listNums.append(num)
	print("En forma ascendente: ")
	for num in listNums:
		print(num)
	listNums.sort(reverse=True)
	print("En forma descendente: ")
	for num in listNums:
		print(num)
		
secImpares()
