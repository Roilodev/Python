# Variables

my_string_variable = 'My string variable'
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = False
print(my_bool_variable)

my_list_variable = ['1','2','3']
print(my_list_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

# Concatenación de variables en un print
print(my_string_variable, str(my_int_variable), my_int_variable, my_bool_variable)
print("Esta es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea. Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Brais", "More", "MoureDev", 35
print("Me llamo: ", name, surname, ".Mi edad es:", age, ".Y mi alias:", alias )

""" # Imputs
name = input('What is your name? ')
age = input('How old are you? ')

print(name)
print(age) """

# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(type(address)) # Cambia el tipo!