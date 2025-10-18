suma = 0
contador = 0

while True:
    numero = input("Ingresa un número (o 'fin' para terminar): ")
    if numero.lower() == 'fin':
        break
    numero = float(numero)
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
    print("La media de los números ingresados es:", media)
else:
    print("No se ingresaron números.")
