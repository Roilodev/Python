# File Handling

# .txt file
import os


txt_file = open("Intermediate/my_file.txt", "w")  # write mode
txt_file.write("Mi nombre es Brais\n")
txt_file.write("Mi apellido es Moure\n")
txt_file.write("Mi edad es 35\n")
txt_file.write("Mi lenguaje de programacion favorito es Python\n")

txt_file.close()

txt_file = open("Intermediate/my_file.txt", "r")  # read mode
for line in txt_file.readlines():
    print(line.strip())  # strip() removes leading and trailing whitespace

txt_file.close()
os.remove("Intermediate/my_file.txt")  # remove the file

# .json file
import json

json_file = open("Intermediate/my_file.json", "w")  # write mode
json_file.write('{"name": "Brais", "surname": "Moure", "age": 35, "language": "Python"}')