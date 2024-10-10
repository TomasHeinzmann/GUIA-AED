import random
def lanzarDados ():
	dado1 = random.randint(1, 6)
	dado2 = random.randint(1, 6)
	suma = dado1 + dado2
	if (dado1 == dado2) or (suma % 2 != 0):
		print("Gano el jugador!")
	else:
		print("Gana la maquina!") 


