import random

class Temperatura:
	
	def __init__(self):
		self.region = random.choice(("Entre rios", "Tucuman", "Jujuy", "Buenos Aires", "Cordoba"))
		self.mes = random.randint(1, 12)
		self.maxima = random.randint(35, 45)
		self.minima = random.randint(1, 10)
	 
	def __str__(self):
		return f"Region: {self.region} | Mes: {self.mes} | Minima: {self.minima} | Maxima: {self.maxima}"
		
