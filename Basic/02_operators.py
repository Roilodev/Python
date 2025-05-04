# Operadores aritmeticos

print(3 + 4) # suma 
print(3 - 4) # resta
print(3 * 4) # multiplicacion
print(3 / 4) # division
print(10 // 3) # division aproximada
print(10 % 3) # modulo
print(2 ** 3) # exponente

print("Hola" + " Python" + " Que tal?") # concatenar
# print("Hola" + 5) # Error
print("Hola " + str(5))

print(3 ** 2 + 3 - 2 // 4) # combinadas

print("Hola "*5) # repetir cadena
my_float = 2.5 * 2
print("Hola "*int(my_float))

# Operadores comparativos con numeros
print(3 > 4) # False
print(3 < 4) # True
print(3 <= 4) # True
print(3 >= 4) # False
print(3 == 4) # False
print(3 != 4) # True
print(10 > 9 < 8) #False 

# operadores comparacion alfabetica por ASCII
print("Hola" > "Python") # False
print("Hola" < "Python") # True
print("Hola" <= "Python") # True
print("Hola" >= "Python") # False
print("Hola" == "Python") # False
print("Hola" != "Python") # True
print("babi">="abuelo") # True

# operadores logicos (and, or, and not)
print(3 > 4 and 'Hola' > 'Python') # False
print(3 > 4 or 'Hola' > 'Python') # False
print(not 3 > 4) # True