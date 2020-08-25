def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1,2,3,4,5,6)

    for i in range(10):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number("not in the list")

catch_this()
