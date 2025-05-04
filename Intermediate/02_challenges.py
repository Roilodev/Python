# Challenge

# El famoso FIZZ BUZZ
# Escribe un programa que imprima los números del 1 al 100, pero para múltiplos de tres imprime "Fizz" 
# en lugar del número y para los múltiplos de cinco imprime "Buzz". Para los números que son múltiplos 
# de tres y cinco, imprime "FizzBuzz".

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Es un anagrama?
# Escribe una función que determine si dos cadenas son anagramas entre sí.
# Un anagrama es una palabra o frase que se forma reorganizando las letras de otra palabra o frase,
# utilizando todas las letras originales exactamente una vez.
def son_anagramas(cadena1, cadena2):
    # Convertir las cadenas a minúsculas y eliminar espacios
    cadena1 = cadena1.replace(" ", "").lower()
    cadena2 = cadena2.replace(" ", "").lower()
    
    # Ordenar las letras de ambas cadenas y compararlas
    return sorted(cadena1) == sorted(cadena2)

# Ejemplo de uso
cadena1 = "amor"
cadena2 = "roma"
if son_anagramas(cadena1, cadena2):
    print(f"{cadena1} y {cadena2} son anagramas.")
else:
    print(f"{cadena1} y {cadena2} no son anagramas.")

# Palíndromo
# Escribe una función que determine si una cadena es un palíndromo.
# Un palíndromo es una palabra, frase o número que se lee igual hacia adelante y hacia atrás.
def es_palindromo(cadena):
    # Convertir la cadena a minúsculas y eliminar espacios y caracteres especiales
    cadena = ''.join(filter(str.isalnum, cadena)).lower()
    
    # Comparar la cadena con su reverso
    return cadena == cadena[::-1]

print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("Hola"))  # False
print(es_palindromo("Amigo"))  # False
print(es_palindromo("Amo la pacífica paloma"))  # True  

# Fibonacci
# Escribe una función que genere la secuencia de Fibonacci hasta un número n dado.
# La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos anteriores.
# Los primeros números de la secuencia son 0 y 1.
def fibonacci(n):
    secuencia = [0, 1]
    while True:
        siguiente = secuencia[-1] + secuencia[-2]
        if siguiente > n:
            break
        secuencia.append(siguiente)
    return secuencia

print(fibonacci(100))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Factorial
# Escribe una función que calcule el factorial de un número n dado.
# El factorial de un número n es el producto de todos los números enteros desde 1 hasta n.
# Se denota como n!.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))  # 120

# Palíndromo numérico
# Escribe una función que determine si un número es un palíndromo.
# Un palíndromo numérico es un número que se lee igual hacia adelante y hacia atrás.
def es_palindromo_numerico(numero):
    # Convertir el número a cadena y comparar con su reverso
    return str(numero) == str(numero)[::-1]

print(es_palindromo_numerico(12321))  # True