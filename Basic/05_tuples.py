# Tuples

my_tuple = tuple()
my_other_tuple = (30, 15, 40)

my_tuple = (35, 1.77, "Brais", "Moure", "Brais")
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("MoureDev"))
print(my_tuple.index("Moure"))

# my_tuple[1] = 1.80 # TypeError: 'tuple' object does not support item assignment

# Para poder modificar tuplas hay que convertirlas en lista.
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple.insert(1, "Azul")
print(my_tuple)

# Se retorna a tupla
my_tuple = tuple(my_tuple)

del my_tuple # Con esto se elimina la variable
print(my_tuple) # NameError: name 'my_tuple' is not defined