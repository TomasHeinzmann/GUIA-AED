import random

class Maquina:
	def __init__(self):
		self.ip_envio = random.randint(100000000, 400000000)
		self.ip_recibe = random.randint(100000000, 400000000)
		self.bytes = random.randint(256, 4000)
	
	def __str__(self):
		return f"Ip: {self.ip_envio} | A la ip: {self.ip_recibe} | bytes enviados: {self.bytes}"
