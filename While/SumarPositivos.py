suma = 0

while True:
    numero = float(input("Ingresa un número positivo (o un número negativo para salir): "))
    if numero < 0:
        break  
    suma += numero

print("La suma de los números positivos es:", suma)
