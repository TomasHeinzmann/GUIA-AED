import random

def piedraPapelTijeras():
	print("---------- PIEDRA PAPEL O TIJERAS ----------")
	jugador = int(input("Ingrese una opcion (1-papel, 2-tijeras o 3-piedra): "))
	maquina = random.randint(1, 3)
	if jugador == 1 and maquina == 2:
		print("Gano el jugador!")
		print("Gana papel!")
	elif jugador == 2 and maquina == 1:
		print("Gano el jugador!")
		print("Gana tijeras!")
	elif jugador == 3 and maquina == 2:
		print("Gano el jugador")
		print("Gana piedra!")
	elif jugador == 2 and maquina == 1:
		print("Gano la maquina!")
		print("Gana papel!")
	elif jugador == 1 and maquina == 2:
		print("Gano la maquina!")
		print("Gana tijeras!")
	elif jugador == 2 and maquina == 3:
		print("Gano la maquina!")
		print("Gana piedra!")
	else:
		print("Empate!")

piedraPapelTijeras()
