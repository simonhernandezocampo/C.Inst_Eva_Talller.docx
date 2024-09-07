# Solicitar las notas del estudiante y el costo de la matrícula
nota1 = float(input("Ingrese la primera nota (de 1 a 5): "))
nota2 = float(input("Ingrese la segunda nota (de 1 a 5): "))
nota3 = float(input("Ingrese la tercera nota (de 1 a 5): "))
nota4 = float(input("Ingrese la cuarta nota (de 1 a 5): "))
costo_matricula = float(input("Ingrese el costo total de la matrícula: "))

# Calcular el promedio de las notas
promedio = (nota1 + nota2 + nota3 + nota4) / 4

# Determinar la clasificación del rendimiento
if 4 <= promedio <= 5:
    clasificacion = "Excelente"
    descuento = 0.20
elif 3 <= promedio < 4:
    clasificacion = "Bien"
    descuento = 0.0
else:
    clasificacion = "Deficiente"
    descuento = 0.0

# Calcular el monto final a pagar por la matrícula
monto_final = costo_matricula * (1 - descuento)

# Mostrar los resultados
print(f"Promedio del estudiante: {promedio:.2f}")
print(f"Clasificación de rendimiento: {clasificacion}")
print(f"monto final a pagar por la matricula: {promedio:.2f}")