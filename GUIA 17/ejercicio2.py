import random

def validar(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor no puede ser menor que 0")
		n = int(input(msg))
	return n

def lanzar_dados(n):
	resultados = []
	for i in range(n):
		dado1 = random.randint(1, 6)
		dado2 = random.randint(1, 6)
		resultado = [dado1, dado2]
		resultados.append(resultado)
	return resultados

def mismos_dados(v):
	cont = 0
	for i in range(len(v)):
		if v[i][0] == v[i][1]:
			cont += 1
	porc = cont * 100 // len(v)
	return porc

def dados_impares(v):
	for i in range(len(v)):
		if v[i][0] % 2 != 0 and v[i][1] % 2 != 0:
			print(f"En el lanzamiento {i+1} hubo dos dados impares!")
			break
	
def mayores_dados(v):
	dado1 = [0, 0]; dado2 = [0, 0]
	for i in range(len(v)):
		if v[i][0] > dado1[0]:
			dado1[0] = v[i][0]
		elif v[i][1] > dado2[0]:
			dado2[0] = v[i][0]
	for i in range(len(v)):
		if v[i][0] == dado1[0]:
			dado1[1] += 1
		elif v[i][1] == dado2[0]:
			dado2[1] += 1
	print(f"El mayor valor que aparecio en el primer dado es {dado1[0]}")
	print(f"Cantidad de veces que aparecio {dado1[1]} veces")
	print(f"El mayor valor que aparecio en el primer dado es {dado2[0]}")
	print(f"Cantidad de veces que aparecio {dado2[1]} veces")

def contar_sumas(v):
	contador = [0] * 12
	for dados in v:
		suma = dados[0] + dados[1]
		contador[suma-1] += 1
	return contador
	
def promedio_y_mayor(v):
	acum = 0; cant = 0
	for dados in v:
		suma = dados[0] + dados[1]
		acum += suma
	prom = acum / len(v)
	for dados in v:
		suma = dados[0] + dados[1]
		if suma > prom:
			cant += 1
	return cant

def principal():
	n = validar("Ingrese cantidad de tiradas de dados: ")
	v = lanzar_dados(n)
	porc = mismos_dados(v)
	print(f"Porcentaje de dados con los mismos resultados: {porc}%")
	dados_impares(v)
	mayores_dados(v)
	contador = contar_sumas(v)
	print(v)
	print(contador)
	cant = promedio_y_mayor(v)
	print(cant)

if __name__ == "__main__":
	principal()
