# Inicializamos las variables
sum_edad_hombres = 0
sum_edad_mujeres = 0
sum_edad_total = 0
cantidad_hombres = 0
cantidad_mujeres = 0
cantidad_total = 0

# Leemos las edades y sexos de los alumnos
for i in range(10):  # Suponemos que hay 10 alumnos
    edad = int(input("Ingrese la edad del alumno: "))
    sexo = input("Ingrese el sexo del alumno (hombre/mujer): ")

    # Sumamos las edades y contamos la cantidad de hombres y mujeres
    if sexo.lower() == "hombre":
        sum_edad_hombres += edad
        cantidad_hombres += 1
    elif sexo.lower() == "mujer":
        sum_edad_mujeres += edad
        cantidad_mujeres += 1
    sum_edad_total += edad
    cantidad_total += 1

# Calculamos los promedios
promedio_hombres = sum_edad_hombres / cantidad_hombres
promedio_mujeres = sum_edad_mujeres / cantidad_mujeres
promedio_total = sum_edad_total / cantidad_total

# Imprimimos los promedios
print(f"Promedio de edad de hombres: {promedio_hombres}")
print(f"Promedio de edad de mujeres: {promedio_mujeres}")
print(f"Promedio de edad del grupo total: {promedio_total}")

