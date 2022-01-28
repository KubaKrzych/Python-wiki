"""
Lambdas
Basically, a one line function. Commonly used in data structure sorting e.g. dictionaries.
"""

def square(x: float):
    return x * x
square_lamba = lambda x: x * x
result_from_func = square(5)
result_with_lambda = square_lamba(5)
# print("Value from lambda:{}\nValue from function: {}\n".format(result_with_lambda, result_from_func))


my_list = [4, 2, 17, 1/2, 0.75, 3,14]
my_list.sort(key=lambda x: x**(0.5)) # Numbers sorted by their roots
# print(f"List sorted by square roots of its elements:\n{my_list}")

apartments = {"326": 8017, "913": 4097, "131": 1300, "911": 6319}  # Apartments and their access code
# print( sorted(apartments.items(), key=lambda x: x) )  # Sorted by apartments
# print( sorted(apartments.values(), key=lambda x: x) ) # Sorted by codes to the apartments


# Below we've got ourselves a list of tuples containing information about a specific emplyee {name, surname, age}
employees = [("Patrick", "Wall", 31), ("Mathew", "Williams", 23), ("Judy", "Snyder", 27), ("Patricia", "Keys", 35)]
# print( sorted(employees, key=lambda employee: employee[2]) )  # Sorted employees by their age
