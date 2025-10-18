precio = float(input("Ingresa el precio del artículo: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

precio_final = precio - (precio * (descuento / 100))

print("El precio después del descuento es:", precio_final)
