#iniciamos las variables
sumCalif = 0
max = 0
min = 100

#leemos las calificaciones
for i in range (20):
    calif = float(input("ingrese la calificacion del alumno {}:"))
    sumCalif += calif
#verificamos si la calificacion es mas alta o mas baja que las anteriores 
    if calif > max:
        max = calif
    elif calif < min:
        min = calif
#calculamos el promedio 
promedio = sumCalif / 20
#imprimimos los resultados 
print(f"promedio del grupo: {promedio}")
print(f"calificacion mas baja: {min}")
print(f"calificacion mas alta: {max}")    
