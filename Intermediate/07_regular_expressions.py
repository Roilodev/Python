# Regular expressions

import re

my_string = "Esta es la lección número 7: Lección Expresiones regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string)  # match the string "Expresiones" in my_string
print(match)  # print the match object
print(match.group())  # print the matched string
print(match.span())  # print the start and end position of the match
print(match.start())  # print the start position of the match
print(match.end())  # print the end position of the match

start, end = match.span()  # get the start and end position of the match
print(my_string[start:end])  # print the matched string using the start and end position

# Search
match = re.search("Expresiones", my_string)  # search the string "Expresiones" in my_string
print(match)  # print the match object
print(match.group())  # print the matched string
print(match.span())  # print the start and end position of the match

print(match.start())  # print the start position of the match
print(match.end())  # print the end position of the match

print(my_string[match.start():match.end()])  # print the matched string using the start and end position
print(my_string[match.span()[0]:match.span()[1]])  # print the matched string using the span method

# Findall
match = re.findall("lección", my_string)  # find all occurrences of the string "lección" in my_string, ignoring case
print(match)  # print the list of matched strings
print(type(match))  # print the type of the match object
print(len(match))  # print the number of matched strings

print(my_string.count("lección"))  # print the number of matched strings using the count method
print(re.split(":", my_string))  # split the string using the ":" character as the separator
print(re.split(":", my_string)[1])  # print the second element of the list returned by the split method

print(re.sub("lección", "lección 7", my_string))  # replace the string "lección" with "lección 7" in my_string
print(re.sub("lección", "lección 7", my_string, count=1))  # replace the first occurrence of the string "lección" with "lección 7" in my_string
print(re.sub("lección|Lección", "LECCIÓN", my_string, count=1))  # replace the first occurrence of the string "lección" or "lección" with "lección 7" in my_string
print(re.sub("[l|L]ección", "lección 7", my_string, count=1))  # replace the first occurrence of the string "lección" or "lección" with "lección 7" in my_string

