def duracionVuelo(partida, llegada):
	horaPartida = int(partida[0] + partida[1])
	minPartida = int(partida[3] + partida[4]) + horaPartida * 60
	horaLlegada = int(llegada[0] + llegada[1])
	minLlegada = int(llegada[3] + llegada[4]) + horaLlegada * 60
	diferencia = abs(minPartida - minLlegada)
	llegadaHoraHotel = (minLlegada + 45) // 60
	llegadaMinHotel = (minLlegada + 45) % 60
	print(f"Duracion del viaje: {diferencia} minutos")
	print(f"Tomando en cuenta la llegada al hotel llega a las {str(llegadaHoraHotel)}:{str(llegadaMinHotel)}")

fecha1 = input("Ingrese horario de salida: ") 
fecha2 = input("Ingrese horario de llegada: ")

duracionVuelo(fecha1, fecha2)
