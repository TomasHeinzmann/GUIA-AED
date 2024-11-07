from maquinas import Maquina

def menu():
	print("************************MENU DE OPCIONES************************")
	print("1) Buscar cantidad de bytes de una ip")
	print("2) Mostrar datos de la maquina que menos bytes envio")
	print("3) Saber cantidad de veces que recibio informacion una ip dada")
	print("0) ~ Salir ~")
	print("----------------------------------------------------------------")
	opc = int(input("Ingrese una opcion: "))
	while opc > 3 or opc < 0:
		print("Error. La opcion ingresada es invalida")
		opc = int(input("Ingrese una opcion: "))
	return opc

def principal():
	


if __name__ == "__main__":
	principal()
