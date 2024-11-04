import random

def validar_n(msg):
	n = int(input(msg))
	while n <= 0:
		print("Error. El valor ingresado no puede ser menor o igual a cero")
		n = int(input(msg))
	return n



def generar_arreglo(n):
	v = []
	nombres = ["dario", "tomas", "nicolas", "flor", "julieta", "emilia", "claudio", "ignacio", "vanina", "agostina", "nilda"]
	for i in range(n):
		randNom = random.choice(nombres)
		while randNom in v:
			randNom = random.choice(nombres)
		v.append(randNom)
	return v

def ingresar_nombres(n):
	v = []
	for i in range(n):
		nombre = input("Ingrese un nombre de usuario: ")
		while nombre in v:
			print("Error. El nombre ya se encuentra en la lista")
			nombre = input("Ingrese un nombre de usuario: ")
		v.append(nombre)
	return v

def principal():
	n = validar_n("Ingrese cantidad de usuarios a crear: ")
	v = generar_arreglo(n)
	j = ingresar_nombres(n)


if __name__ == "__main__":
	principal()
