# DOC STRING, TYPE HINT
# def print_hello(name: str) -> str:
#     """
#     Returns a greetings
#     Paramaters:
#         name(str): The name of the person
#     Returns:
#         The cool message!!
#     """
#     print('hello, '+ name)

# print_hello("Rupesh")

# LAMDA FUNCTION
# presenters = [
#     {'name':'susan', 'age':50},
#     {'name':'Christopher', 'age':47}
# ]
# presenters.sort(key=lambda item: item['name'])
# print(presenters)

# class Presenter():
#     def __init__(self, name):
#         #constructor
#         self.name = name
    
#     def say_hello(self):
#         #method
#         print('Hello, '+ self.name)

# presenter = Presenter('Rupesh')
# presenter.say_hello()

class Presenter():
    def __init__(self, name):
        #constructor
        self.name = name #field to store the value or to build the base property
#setting up the property "name" #and property is setup using the setter 
    @property
    def name(self):
        """
        This getter will be called when getting the user asked vlue. Example x = presenter.name
        """
        return self.__name

    @name.setter
    def name(self, value):
        #cool validation here
        """"
        This setter will be called when setting up the value for the properties
        presenter.name ='Christopher'
        """
        self.__name = value
presenter= Presenter('Rupesh')
presenter.name = 'Harkey'
print(presenter.name)