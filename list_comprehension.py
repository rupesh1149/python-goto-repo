# list comprehension technique used for looping over something to give specific result and producing a list of new result
import types
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = [int(number) for number in numbers if number > 0]
print(newlist)
