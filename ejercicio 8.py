#iniciamos las variables de conteo 
menor_50 = 0
entre_50_70 = 0
entre_70_80 = 0
mayor_80 = 0

#leemos las calificaciones de los estudiantes 
for i in range (23):
    calificacion = float(input("ingrese la calificacion del estudiante: "))

#verificamos en que rango se encuentra la calificacion
if calificacion < 50:
    menor_50 += 1
elif 50 <= calificacion < 70:
    entre_50_70 += 1
elif 70 <= calificacion < 80:
    entre_70_80 += 1
else:
    mayor_80 += 1

#imprimimos los resultados
print(f"cantidad de estudiantes que obtuvieron una calificacion menor a 50: {menor_50}")
print(f"cantidad de estudiantes que obtuvieron de 50 o más pero menor que 70: {entre_50_70}")
print(f"Cantidad de estudiantes que obtuvieron una calificación de 70 o más pero menor que 80: {entre_70_80}")
print(f"Cantidad de estudiantes que obtuvieron una calificación de 80 o más: {mayor_80}")
