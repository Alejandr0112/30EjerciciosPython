calificacion = int(input("Ingresa la calificación (0-100): "))

if calificacion >= 90 and calificacion <= 100:
    print("Calificación: A")
elif calificacion >= 80 and calificacion <= 89:
    print("Calificación: B")
elif calificacion >= 70 and calificacion <= 79:
    print("Calificación: C")
elif calificacion >= 60 and calificacion <= 69:
    print("Calificación: D")
elif calificacion >= 0 and calificacion <= 59:
    print("Calificación: F")
else:
    print("Error: la calificación debe estar entre 0 y 100.")
