# Condiotionals

my_condition = False

if my_condition:
    print("Se ejecuta la condición del if")

my_condition = 5 * 5

if my_condition == 10:
    print("Se ejecuta la condición del segundo if")

if my_condition >= 10:
    print("Se ejecuta la condición del tercer if")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25 :
    print("Es igual al 25")
else:    
    print("Es menor que 10 o mayor o igual que 20 y distinto de 25")
    
print("La ejecución continúa")

my_string = "Mi cadena de texto"

if my_string:
    print("Mi cadena de texto es vacía")