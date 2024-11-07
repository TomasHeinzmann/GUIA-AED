
def ingresar_atletas():
	atletas = [None] * 3 
	for i in range(3):
		print(f"Ingrese datos del atleta numero {i+1}")
		nombre = input("Ingrese nombre: ")
		tNatacion = float(input("Ingrese tiempo de natacion: "))
		tCiclismo = float(input("Ingrese tiempo de cliclismo: "))
		tCorriendo = float(input("Ingrese tiempo corriendo: "))
		atletas[i] = [nombre, tNatacion, tCiclismo, tCorriendo]
	return atletas

def promedio_atletas(atletas):
	tiempo = [0] * 3
	for i in range(len(atletas)):
		tiempo[i] += atletas[i][1] + atletas[i][1] + atletas[i][1]
		tiempo[i] /= 3
	return tiempo
	
def mostrar_promedio(promedio_total, atletas):
	for i in range(len(promedio_total)):
		print("-----------------------------------------------------")
		print(f"El atleta {atletas[i][0]} tuvo un promedio total de:")
		print(f"{promedio_total[i]} minutos")

def determinar_podio(promedio_total, atletas):
	primero = promedio_total.index(min(promedio_total))
	segundo = None
	tercero = promedio_total.index(max(promedio_total))
	for i in range(len(promedio_total)):
		if i != primero and i != tercero:
			segundo = i
	print(f"El primer puesto es para {atletas[primero][0]}!!!")
	print(f"El segundo puesto es para {atletas[segundo][0]}!!")
	print(f"El tercero puesto es para {atletas[tercero][0]}!")
	

def principal():
	atletas = ingresar_atletas()
	promedio_total = promedio_atletas(atletas)
	mostrar_promedio(promedio_total, atletas)
	determinar_podio(promedio_total, atletas)
	

if __name__ == "__main__":
	principal()
