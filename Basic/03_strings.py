# Strings
my_string = "Mi string"
my_other_string = 'Mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linea"
print(my_new_line_string)

my_tab_string = "\tEste es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\tEste es un string \\n escapado"
print(my_scape_string)

# formateo!!!
name, surname, age = "Brais", "Moure", 35
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
# ValueError: too many values to unpack (expected 2)
""" language = "Python"
a, b = language
print(a)
print(b) """

language = "python"
a, b , c, d , e, f = language
print(a+b+c+d+e+f)

# División
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse (nohtyP)
reverse_language = language[::-1]
print(reverse_language)

# Funciones
print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print(language.lower())
print(language.lower().isupper())
print("2".isnumeric())
print(language.startswith("Py"))