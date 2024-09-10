#Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números.
negativos = 0 
for i in range(0, 20): #se crea un bucle de los numeros que queremos convertir
    num = int(input("ingrese numeros negativos: ")) #pedimos que nos que nos ingresen los numeros que pedimos
    if num < 0:
        negativos += num * -1
#se imprime el reultado final
print(f"la suma de los numeros negativos convertidos a positivos son:{negativos}")