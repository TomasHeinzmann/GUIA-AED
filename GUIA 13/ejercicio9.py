
def porcentaje(a, b):
	if b != 0:
		return a * 100 / b
	else:
		return 0

def obtener_menor(a, b):
	return min(a, b)

def contar_si(a, b):
	if a:
		return b + 1
	else:
		return b 

def proceso_de_cadenas():
	texto = input("Ingrese texto: ")
	vocales = "AaáÁEeéÉIiíÍOoóÓUuúÚ"; cant_vocales = 0
	cant_consonantes = 0; palabras_totales = 0
	palabras_mas_vocales = 0; letras = 0; menor = 1000
	letra_anterior = None; flag_svocal = False; punto3 = 0
	punto4 = 0; flag_letras_iguales = False; punto2 = 10000
	for letra in texto:
		if letra == " " or letra == ".":
			palabras_totales += 1
			if cant_vocales > cant_consonantes:
				palabras_mas_vocales += 1
			punto2 = obtener_menor(letras, punto2)
			punto3 = contar_si(flag_svocal, punto3)
			punto4 = contar_si(flag_letras_iguales, punto4)
			flag_svocal = False; letras = 0
			cant_consonantes = 0; cant_vocales = 0
			flag_letras_iguales = False
		else:
			letras += 1
			if letras == 1 and letra == letra_anterior:
				flag_letras_iguales = True
			if letra in vocales:
				cant_vocales += 1
			else:
				cant_consonantes += 1
			if letra_anterior != None and letra_anterior in "Ss" and letra in vocales:
				flag_svocal = True
			letra_anterior = letra
	punto1 = porcentaje(palabras_mas_vocales, palabras_totales)
	print(f"Porcentaje de palabras con más vocales que consonantes: {punto1}%")
	print(f"Cantidad de caracteres de la palabra con menor cantidad de caracteres del texto: {punto2}")
	print(f"Cantidad de palabras que tuvieron al menos una vez la secuencia 's' + vocal: {punto3}")
	print(f"Cantidad de palabras que comenzaron el último caracter de la palabra anterior: {punto4}")
	


if __name__ == "__main__":
	proceso_de_cadenas()
