#Calcular la cantidad de hombres y mujeres presentes en un salón de clases con untotal de n personas.
hombres = 0 #iniciamos con un contador para las mujeres y uno para los hombres
mujeres = 0
perSalon =int(input("ingrese el total de personas en un salon: ")) #pedimos que ingrese el total de personas que hay en el salon
#hacemos un bucle que inicie de 0 hasta el numero de personas que ingreso el usuario
for i in range (perSalon):
    genero= input("ingrese su genero (MUJER/HOMBRE): ") #pedimos que ingrese el genero
    if genero == "mujer": #si es mujer el contador incrementa 1 al contador de mujeres
        mujeres += 1
    elif genero == 'hombre': #si es hombre el contador de hombres incrementa 1
        hombres += 1
#se imprimen los resultados 
print(f"la cantidad de hombres es: {hombres}, la cantidad de mujeres es: {mujeres}, la cantidad de personas en el salon es: {perSalon}")


