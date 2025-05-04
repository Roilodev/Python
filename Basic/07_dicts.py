# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

# Se definen como relación clave:valor
my_other_dict = {
    "Nombre":"Brais",
    "Apellidos":"Moure",
    "Edad":35,
    1:"Python"
}

my_dict = {
    "Nombre":"Brais",
    "Apellidos":"Moure",
    "Edad":35,
    "Lenguajes":{"Python", "Swift", "Kotlin"},
    1:1.77
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle MaureDev"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Moure" in my_dict["Apellidos"]) # Si no se define el ["valor"] la búsqueda se realiza por la clave

# operaciones
print(my_dict.items()) # dict_items([('Nombre', 'Pedro'), ('Apellidos', 'Moure'), ('Edad', 35), ('Lenguajes', {'Swift', 'Python', 'Kotlin'}), (1, 1.77)])
print(my_dict.keys()) # dict_keys(['Nombre', 'Apellidos', 'Edad', 'Lenguajes', 1])
print(my_dict.values()) # dict_values(['Pedro', 'Moure', 35, {'Swift', 'Python', 'Kotlin'}, 1.77])

my_new_dict = dict.fromkeys(("Nombre", 1))
print(my_new_dict)

my_new_dict["Nombre"] = "Moure"
my_new_dict[1] = 2.00
my_new_dict["Calle"] = "Calle Moure"

print(my_new_dict)

my_list = ["Nombre", "Edad", "Calle"]
my_second_dict = dict.fromkeys(my_list)
print(my_second_dict)

my_second_dict = dict.fromkeys(my_dict)
print(my_second_dict)

my_second_dict = dict.fromkeys(my_dict, "MoureDev")
print(my_second_dict)

my_values = my_new_dict.values()
print(type(my_values))

print(list(my_second_dict.values()))
print(tuple(my_second_dict))
print(set(my_second_dict))