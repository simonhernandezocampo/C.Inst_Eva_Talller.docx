def calcular_costo_llamada():
    # Solicitar el destino de la llamada
    destino = input(
        "Ingrese el destino de la llamada (Estados Unidos, Canadá, Europa, Resto del mundo): ").strip().lower()

    # Solicitar la duración de la llamada
    try:
        duracion = float(input("Ingrese la duración de la llamada en minutos: "))
    except ValueError:
        print("Duración inválida. Debe ser un número.")
        return

    # Inicializar el costo por minuto
    if destino == "estados unidos":
        costo_por_minuto = 900
    elif destino == "canadá":
        costo_por_minuto = 800
    elif destino == "europa":
        costo_por_minuto = 950
    elif destino == "resto del mundo":
        costo_por_minuto = 1250

    # Calcular el costo total sin descuento
    costo_total = costo_por_minuto * duracion

    # Aplicar descuento si la duración es mayor a 15 minutos
    if duracion > 15:
        costo_total *= 0.8  # Aplicar un 20% de descuento

    # Mostrar el costo total
    print(f"El costo total de la llamada es: {costo_total:.2f} pesos")


# Ejecutar la función
calcular_costo_llamada()