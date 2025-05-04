# File Handling

# .txt file
import os

txt_file = open("Intermediate/my_file.txt", "w")  # write mode
print("\n*** Fichero txt ***")
txt_file.write("Mi nombre es Brais\n")
txt_file.write("Mi apellido es Moure\n")
txt_file.write("Mi edad es 35\n")
txt_file.write("Mi lenguaje de programacion favorito es Python\n")

txt_file.close()

txt_file = open("Intermediate/my_file.txt", "r")  # read mode
for line in txt_file.readlines():
    print(line.strip())  # strip() removes leading and trailing whitespace

txt_file.close()
# os.remove("Intermediate/my_file.txt")  # remove the file

# .json file
import json

json_file = open("Intermediate/my_file.json", "w")  # write mode

json_test = {
    "name": "Brais",
    "surname": "Moure",
    "age": 35,
    "languages": ["Python", "JavaScript", "Java"],
}

json.dump(json_test, json_file, indent=2)  # dump the json object to the file

json_file.close()

json_file = open("Intermediate/my_file.json", "r")  # read mode
print("\n*** Fichero json ***")

for line in json_file.readlines():
    print(line.strip())  # strip() removes leading and trailing whitespace

json_file = open("Intermediate/my_file.json", "r")  # read mode

my_dict = json.load(json_file)  # load the json object from the file
print(my_dict["name"])  # print the name from the json object

json_file.close()
# os.remove("Intermediate/my_file.json")  # remove the file

# .csv file
import csv

csv_file = open("Intermediate/my_file.csv", "w")  # write mode
csv_writer = csv.writer(csv_file)  # create a csv writer object
csv_writer.writerow(["name", "surname", "age", "languages"])  # write the header
csv_writer.writerow(["Brais", "Moure", 35, ["Python", "JavaScript", "Java"]])  # write the data
csv_writer.writerow(["John", "Doe", 30, ["C++", "C#", "Ruby"]])  # write the data
csv_writer.writerow(["Jane", "Doe", 25, ["PHP", "Swift", "Go"]])  # write the data

csv_file.close()

csv_file = open("Intermediate/my_file.csv")  # write mode
print("\n*** Fichero csv ***")

for line in csv_file.readlines():
    print(line.strip())  # strip() removes leading and

csv_file.close()
# os.remove("Intermediate/my_file.csv")  # remove the file