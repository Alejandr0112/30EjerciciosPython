from datetime import datetime

año = int(input("Ingresa tu año de nacimiento: "))
año_actual = datetime.now().year

if año > 1900 and año < año_actual:
    print("El año de nacimiento es válido.")
else:
    print("El año de nacimiento no es válido.")
