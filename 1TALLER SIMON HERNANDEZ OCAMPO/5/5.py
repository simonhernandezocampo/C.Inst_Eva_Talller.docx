a, b, c, d = 7, 5, 3, 3

# Verificar si a es mayor que b
condicion_1 = a > b

# Verificar si c es igual a d
condicion_2 = c == d

# Comprobar si solo una de las condiciones es verdadera (XOR)
resultado = condicion_1 ^ condicion_2

# Mostrar los resultados
print("a > b:", condicion_1)  # True o False
print("c == d:", condicion_2)  # True o False
print("Solo una de las condiciones es verdadera:", resultado)