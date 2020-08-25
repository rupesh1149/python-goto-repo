# # Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.
# from functools import partial

# def multiply(x,y):
#     print(y)
#     return x*y

# dbl = partial(multiply, 2)
# print(dbl(4))

#Following is the exercise, function provided:
from functools import partial
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
chg = partial(func, 5,5,5)
print(chg(15))