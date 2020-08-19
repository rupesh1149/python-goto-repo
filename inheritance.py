class Person():
    def __init__(self, name):
        #constructor
        self.name = name
    def say_hello(self):
        print ('Hello, '+ self.name)
    #overridding __str__
    def __str__(self):
        return self.name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school=school
    
    def sing_school_song(self):
        print('Ode to '+ self.school)
    
    def say_hello(self):
        #Let the parent do some work
        super().say_hello()
        #Add on custome code
        print('I am a student')
    # overridding the base method and the code below prints out string when we print out the class itself.
    def __str__(self):
        return f'{self.name} attended {self.school}'
student = Student('Rupesh', 'Budhanilkantha School')
print(student)
# student.say_hello()
# student.sing_school_song()
