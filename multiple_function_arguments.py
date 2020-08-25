# multiple arguments passing to the function 
# def foo (first, second, third, *therest):
#     print(f'First:{first}')
#     print(f'Second:{second}')
#     print(f'Third:{third}')
#     print(f'All the rest:{therest}')

# foo(1,2,3,4,5,6,7)

#  passing arguments to a function by keywords so that the order of arguments doesnot matter
def bar(first, second, third, **options):
    if options.get("action") =="sum":
        print(f'The sum is :{first + second + third}')
    
    if options.get("number") == "first":
        return first

result = bar(1,2,3, action ="sum", number = "first")
print(f'Result: {result}')