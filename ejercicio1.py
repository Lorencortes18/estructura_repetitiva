#Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros
positivo = 0
negativo = 0
neutro = 0 
 #leemos los 20 numeros 

for i in range (0, 20): #hacemos un bucle que recorra del 0 al 20
    num = int(input("ingrese un numero: ")) #pedimos que digite o ingrese un numero entero
    if num > 1 :
        positivo +=1
    elif num < 0 :
        negativo += 1
    elif num == 0 or num == 1: 
        neutro += 1

 #verificamos si el numero es positivo, negativo o neutro
    
print(f"los numeros positivos son: {positivo}, los numeros negativos son: {negativo}, y los numeros neutros son: {neutro}")
   
