# List comprehension

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]


my_range = range(8)
print(list(my_range))

# Quiero hacer una lista que guarde los números de la lista original
my_list = [i for i in my_original_list]
print(my_list)

# Quiero hacer una lista que guarde el doble de los números de la lista original
my_list = [i * 2 for i in my_original_list]
print(my_list)

# usando funciones
def double(x):
    return x * 2

my_list = [double(i) for i in my_original_list]
print(my_list)