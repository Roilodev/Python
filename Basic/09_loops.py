# Loops/Bucles/Ciclos

# While
# Se ejecuta mientras la condición sea verdadera

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # opcional
    print("Mi condición es mayor o igual que 10")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Mi condición es 15")
        break # Salir del bucle

# For
# Se ejecuta un número determinado de veces, iterando sobre una secuencia (lista, tupla, diccionario, conjunto o cadena)
# Se puede usar la función range() para crear una secuencia de números

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(element)

my_dict = {
    "Nombre":"Brais",
    "Apellidos":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
}

for key, value in my_dict.items():
    print(key, value)
    print(f"{key}: {value}") # Formato de cadena f-string (Python 3.6+)
else: # opcional
    print("He terminado de iterar el diccionario")

for element in my_dict:
    print(element)
    if element == "Edad":
        print("He encontrado la edad")
        break
else: # opcional
    print("He terminado de iterar el diccionario")

for element in my_dict:
    print(element)
    if element == "Edad":
        print("He encontrado la edad")
        continue
else: # opcional
    print("He terminado de iterar el diccionario")

