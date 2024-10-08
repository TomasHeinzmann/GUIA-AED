todoSegundos = 0.15 + 0.75 + 0.80 + 0.15 + 52 + 2 + 59 + 48 + 60 

totalMinutos = todoSegundos // 60
totalSegundos = todoSegundos % 60
totalCentesimas = (totalSegundos - int(totalSegundos)) * 100

print(f"Tiempo total: {round(totalMinutos)}:{round(totalSegundos)}:{round(totalCentesimas)}")


