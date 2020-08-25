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