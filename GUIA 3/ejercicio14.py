def sumaAngulos():
	grados1 = int(input("Ingrese grados del primer angulo: "))
	minutos1 = int(input("Ingrese minutos del primer angulo: "))
	segundos1 = int(input("Ingrese segundos del primer angulo: "))
	grados2 = int(input("Ingrese grados del segundo angulo: "))
	minutos2 = int(input("Ingrese minutos del primer angulo: "))
	segundos2 = int(input("Ingrese segundos del primer angulo: "))
	
	acumuladorsegundos = acumuladorminutos = 0
	
	sumasegundos = segundos1 + segundos2
	while sumasegundos >= 60:
		acumuladorsegundos += 1
		sumasegundos -= 60
	sumaminutos = minutos1 + minutos2
	while sumaminutos >= 60:
		acumuladorminutos += 1
		sumaminutos -= 60
	sumagrados = grados1 + grados2 + acumuladorminutos
	
	print(f"Angulo resultante: {sumagrados}° {sumaminutos}' {sumasegundos}'' ")
	
sumaAngulos()
