import random

def tirarDado():
	dado = random.randint(1, 6)
	return dado


def definirPuntos(dado):
	if dado == 1:
		return 1
	elif dado == 3:
		return 2
	elif dado == 5:
		return 4
	else:
		return 0

def juegoPuntos():
	i = 0
	multiplicar = True
	puntajeAnterior = ""
	while i < 4:
		puntaje = 0
		if i >= 1: 
			puntajeAnterior = int(input("Ingrese su puntaje anterior: "))
		dado1 = tirarDado()
		dado2 = tirarDado()
		dado3 = tirarDado()
		print(f"Resultado de los dados: {dado1}, {dado2} y {dado3}")
		resultado1 = definirPuntos(dado1)
		resultado2 = definirPuntos(dado2)
		resultado3 = definirPuntos(dado3)
		sumaDados = dado1 + dado2 + dado3
		if sumaDados % 2 == 0 and dado1 == dado2 == dado3 and multiplicar:
			sumaDados *= 2
			print("Se duplicaron los puntos!")
			multiplicar = False
		if puntajeAnterior:
			puntaje += resultado1 + resultado2 + resultado3 + puntajeAnterior
		else:
			puntaje += resultado1 + resultado2 + resultado3
		if puntaje:
			print(f"Puntos obtenidos: {puntaje}")
		else:
			print("No obtuvo puntos en esta tirada")
		i += 1

juegoPuntos()
