# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)

    data_transmitter()

print(transmit_to_space("Test message"))
# Even though the execution of the "transmit_to_space()" was completed, the message was rather preserved. This technique by which the 
# data is attached to some code even after end of those other original functions is called as closures in python