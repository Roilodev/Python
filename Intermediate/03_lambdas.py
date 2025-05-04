# Lambdas

sum_tho_values = lambda first_value, second_value: first_value + second_value
print(sum_tho_values(10, 20))

multiply = lambda first_value, second_value: first_value * second_value
print(multiply(10, 20))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(10)(20, 30))