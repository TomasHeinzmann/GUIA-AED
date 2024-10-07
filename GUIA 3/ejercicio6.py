def salarioCalculo(salario, nombre, area):
	salarioNuevo = salario + salario * 0.08 - salario * 0.025
	print(f"Nombre Empleado: {nombre}")
	print(f"Área funcional: {area}")
	print(f"Salario actual: ${salario}")
	print(f"Nuevo salario: ${salarioNuevo}")

