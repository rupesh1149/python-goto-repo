# The map() function in python has the following syntax:

# map(func, *iterables)

# Where func is the function on which each element in iterables 
# (as many as they are) would be applied on. Notice the asterisk(*)
#  on iterables? It means there can be as many iterables as possible, 
#  in so far func has that exact number as required input arguments.

my_pets = ['alfred', 'tabitha', 'william', 'arla']

uppered_pets = list(map(str.upper, my_pets))

print(uppered_pets)
# ########################################

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1,7)))

print(result)
###############################
my_strings =['a','b','c','d','e']
my_numbers = [1,2,3,4,5]

res_zip = list(map(lambda x,y: (x,y),my_strings, my_numbers))
print(res_zip)

########################
# FILTER 
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)
##############################
# REDUCE 
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]

def custom_sum(first, second):
    return first + second

result = reduce(custom_sum, numbers)
print(result)



from functools import reduce 

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
my_numbers = [4, 6, 9, 23, 5]

map_result = list(map(lambda x: round(x ** 2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)