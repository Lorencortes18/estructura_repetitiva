#leemos el numero del cual queremos la tabla de multiplicar
num = int(input("ingrese el numero para la tabla de multiplicar: "))
#imprimimos la tabla de multiplicar 
print(f"tabla de multiplicar del numero: {num}")

for i in range (1, 11): #hacemos un bucle que recorra del 1 al 10
    producto = num * i #hacemos la opercion 
    print(f"{num}*{i}={producto}") #imprimimos el resultado final