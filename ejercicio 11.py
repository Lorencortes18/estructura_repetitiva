# Inicializamos las variables
cantidad_hombres = 0
cantidad_mujeres = 0
sum_altura_total = 0
cantidad_altura_mayor_170 = 0
cantidad_altura_menor_150 = 0

# Leemos los datos de los alumnos
while True:
    edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))
    if edad == 0:
        break
    sexo = input("Ingrese el sexo del alumno (hombre/mujer): ")
    altura = float(input("Ingrese la altura del alumno: "))
# Sumamos las alturas y contamos la cantidad de hombres y mujeres
    sum_altura_total += altura
    if sexo.lower() == "hombre":
        cantidad_hombres += 1
    elif sexo.lower() == "mujer":
        cantidad_mujeres += 1
 # Contamos la cantidad de alumnos que tienen una altura mayor a 1.70 cm o menor o igual a 1.50 cm
    if altura > 1.70:
        cantidad_altura_mayor_170 += 1
    elif altura <= 1.50:
        cantidad_altura_menor_150 += 1

# Calculamos la altura promedio
altura_promedio = sum_altura_total / (cantidad_hombres + cantidad_mujeres)

# Imprimimos los resultados
print(f"Cantidad de hombres: {cantidad_hombres}")
print(f"Cantidad de mujeres: {cantidad_mujeres}")
print(f"Altura promedio: { altura_promedio}")
print(f"Cantidad de alumnos que tienen una altura mayor a 1.70 cm: {cantidad_altura_mayor_170}")
print(f"Cantidad de alumnos que tienen una altura menor o igual a 1.50 cm: {cantidad_altura_menor_150}")

