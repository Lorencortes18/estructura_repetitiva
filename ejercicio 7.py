#La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué, cuantos entran con calcomanía de cada color. Conociendo el ultimo dígito de la placa de cada carro, se puede determinar el color de la calcomanía utilizando la siguiente relación: 

#iniciamos con un contador para cada color
amarillo = 0
rosa = 0
roja = 0
verde = 0
azul = 0
#creamos un indice 0 que se ira incrementando
i = 0
#pedimos la cantidad de cuantos autos ingresaron
numeCarros = int(input("ingrese la cantidad de cuantos autos entraron: "))
#crearemos un bucle
while i < numeCarros:
    placa = int(input("ingrese el ultimo numero de su placa: "))#se pide que ingrese el ulrimo digito de la placa
    if placa == 1 or placa == 2: #si la placa es 1 o 2 sera de color amarillo
        amarillo += 1 #si es amarillo se  incrementa 1 en el contador amarillo
    elif placa == 3 or placa == 4: #si la plata termina en 3 o 4 es de color rosa
        rosa += 1 #si es rosa se incrementa 1 en el contador rosa
    elif placa == 5 or placa == 6: #si la placa termina en 5 o 6 es rojo
        roja += 1 #si es rojo incrementa 1 en el contador rojo
    elif placa == 7 or placa == 8: #si la placa es terminada por el 7 o 8 es verde 
        verde += 1 #si es verde incrementa 1 en el contador verde
    elif placa == 9 or placa == 0: #si la placa es terminada en 9 o 0 es de color azul
        azul += 1 #si es azul incrementa 1 en el contador 
    else:
        print(f"numero invalido.") #imprime el resultado como invalido si no cumple lo acordado
    
    i += 1 #se ira incrementado el indice hasta que le llegue a la cantidad de carros
    #se imprime elresultado
    print(f"cantidad de autos amarillos: {amarillo}, cantidad de autos rosa: {rosa}, cantidad de autos rojos: {roja}, cantidad de autos verdes: {verde} y cantidad de autos azules: {azul}")


