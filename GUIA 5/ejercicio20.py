def premio():
	mont1 = float(input("Ingrese monto 1: "))
	mont2 = float(input("Ingrese monto 2: "))
	mont3 = float(input("Ingrese monto 3: "))
	
	minMont = min(mont1, mont2, mont3)
	prem = minMont * 0.5
	
	if mont1 > 1000 and mont2 > 1000 and mont3 > 1000:
		prem += prem * 0.1

	print(f"El premio es de ${prem} !!!")


