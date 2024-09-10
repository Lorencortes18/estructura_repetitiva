#"Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona. Las categorías se determinar de acuerdo a la siguiente tabla:"
#se inicia un contador para saber el numero de personas ya sean niños, jovenes, adultos y ancianos.
niños = 0
jovenes = 0
adultos = 0
ancianos = 0        
#se inicia una variable para saber el peso total de cada uno
pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0

#hacemos un bucle que recorra del 1 al 51
for i in range(1, 51):
    edades = int(input("ingrese su edad: ")) #pedimos que ingresen el numero de edades 
    pesos = int(input("ingrese su peso: ")) #pedimos que ingresen el peso

    if 0 <= edades <= 12:  #identifica si el rango es de 0 a 12
        niños += 1      #contador niños   
        pesoNiños += pesos  #suma el peso ingresado al acomulador 
    elif 13 <= edades <= 29: #identifica si el rango es de 13 a 29
        jovenes += 1     #contador jovenes
        pesoJovenes += pesos #suma el peso ingresado al acomulador
    elif 30 <= edades <= 59: #identifica si el rango es de 30 a 59
        adultos += 1 #contador adultos
        pesoAdultos += pesos #suma el peso ingresado al acomulador 
    elif edades >= 60: #identifica si el rango es de 60 o ma
        ancianos += 1 #contador ancianos
        pesoAncianos += pesos #suma el peso ingresado al acomulador 
        
promedioNiño = pesoNiños / niños #calcula el promedio de los niños
promedioJovenes = pesoJovenes / jovenes #calcula el promedio de los jovenes 
promedioAdultos = pesoAdultos / adultos #calcula el promedio de los adultos
promedioAncianos = pesoAncianos / ancianos #calcula el promedio de los ancianos 
 #imprimimos el resultado
print(f"El promedio de los niños: {promedioNiño}, el promedio de los Jovenes: {promedioJovenes}, el promedio de los adultos: {promedioAdultos} y el promedio de los ancianos: {promedioAncianos}")

