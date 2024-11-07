
class Punto:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __str__(self):
		return str(self.x) + " ; " + str(self.y)
		
	def determinar_cuadrante(self):
		if self.x > 0 and self.y > 0:
			cuadrante = 1
		elif self.x < 0 and self.y > 0:
			cuadrante = 2
		elif self.x < 0 and self.y < 0:
			cuadrante = 3
		elif self.x > 0 and self.y < 0:
			cuadrante = 4
		return cuadrante

def principal():
	print("Punto 1")
	x = int(input("Ingrese valor de x: "))
	y = int(input("Ingrese valor de y: "))
	Punto1 = Punto(x, y)
	print("Punto 2")
	x = int(input("Ingrese valor de x: "))
	y = int(input("Ingrese valor de y: "))
	Punto2 = Punto(x, y)
	
	cuadrante1 = Punto1.determinar_cuadrante()
	cuadrante2 = Punto2.determinar_cuadrante()
	
	print(f"El punto {Punto1} esta en el cuadrante {cuadrante1}")
	print(f"El punto {Punto2} esta en el cuadrante {cuadrante2}")
	
if __name__ == "__main__":
	principal()
		
