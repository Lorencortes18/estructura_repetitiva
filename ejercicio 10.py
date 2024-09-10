#inicializamos el producto
#"Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo:(1*2*3*4*5...)."
producto = 1
#multiplicamos los 20 primeros numeros naturales
for i in range (1, 21):
    producto = producto * i
#imprimimos el resultado
print(f"el producto de los 20 primeros numeros naturales es: {producto}")