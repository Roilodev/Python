# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [24, 35, 62, 52, 30, 30, 17]
print(len(my_list))

my_other_list = [35, 1.77, "Brais", "Moure"]
print(type(my_other_list))
print(type(my_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
# print(my_other_list[4]) # IndexError: list index out of range

print(my_list.count(30))

# age, height, name = my_other_list # ValueError: too many values to unpack (expected 3)
age, height, name, surname = my_other_list
print(name)

print(my_list + my_other_list) # Concatenar listas

""" # Tipado dinámico
my_list = "Hola Python"
print(type(my_list)) """

# operaciones con listas
my_other_list.append("MoureDev")
print(my_other_list)

my_other_list.insert(1, "Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

my_other_list[1] = 'Rojo'
print(my_other_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:2])