# ~ Una empresa de estadisticas nos solicito un programa sencillo que nos permita obtener los resultados de una competencia del Triatlon Ironman. Dicho programa debe cargar, a modo de prueba, los nombres y tiempos de 3 competidores expresados en hh:mm:ss (Considerar que si la hora, minuto o segundo es menor a 10 agregarle un cero al inicio), a partir de esa carga determinar:
# ~ 1 - El tiempo promedio entero de la prueba
# ~ 2 - Mostrar como quedo conformado el podio en base a esos tres tiempos
# ~ 3 - Indicar con un mensaje, si el tiempo ganador fue superior al tiempo promedio de la prueba

def triatlonIronMan():
	competidores = []
	tiempoSegundos = []
	for i in range(3):
		print(f"Competidor {i+1}")
		nombre = input("Ingrese nombre del competidor: ")
		tiempo = input("Ingrese tiempo (formato de hh:mm:ss): ")
		competidor = [nombre, tiempo]
		competidores.append(competidor)
	
	for competidor in competidores:
		horas = competidor[1][0] + competidor[1][1]
		horas = int(horas) * 3600
		minutos = competidor[1][3] + competidor[1][4]
		minutos = int(minutos) * 60
		segundos = competidor[1][6] + competidor[1][7]
		segundos = int(segundos)
		tiempo = horas + minutos + segundos
		tiempoSegundos.append(tiempo)
		
	promTime = 	(tiempoSegundos[0] + tiempoSegundos[1] + tiempoSegundos[2]) / 3
	
	segundosProm = promTime
	
	horasProm = int(segundosProm // 3600)
	segundosProm -= horasProm * 3600
	minProm = int(segundosProm / 60)
	segundosProm -= minProm * 60
	
	promTimeStr = f"{round(horasProm)}:{round(minProm)}:{round(segundosProm)}"
	
	mayTime = max(tiempoSegundos[0], tiempoSegundos[1], tiempoSegundos[2])
	minTime = min(tiempoSegundos[0], tiempoSegundos[1], tiempoSegundos[2])
	
	if tiempoSegundos[0] != mayTime and tiempoSegundos[0] != minTime:
		midTime = tiempoSegundos[0]
	elif tiempoSegundos[1] != mayTime and tiempoSegundos[1] != minTime:
		midTime = tiempoSegundos[1]
	else:
		midTime = tiempoSegundos[2]
	
	ultimo = tiempoSegundos.index(mayTime)
	segundo = tiempoSegundos.index(midTime)
	primero = tiempoSegundos.index(minTime)
	
	print(f"El primer puesto es para {competidores[primero][0]} con un tiempo de {competidores[primero][1]}")
	print(f"El segundo puesto es para {competidores[segundo][0]} con un tiempo de {competidores[segundo][1]}")
	print(f"El tercer puesto es para {competidores[ultimo][0]} con un tiempo de {competidores[ultimo][1]}")
	
	print(f"El tiempo promedio fue de {promTimeStr}")
	
	if minTime > promTime:
		print("El tiempo ganador fue mayor que el promedio!")
