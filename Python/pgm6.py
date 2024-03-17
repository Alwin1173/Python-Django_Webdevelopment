class Person: #P should be capital in other languages but not in python Person is a the constructor
    def __init__(self,name): #init method or constructor
        self.name=name
    #Sample methode
    def say_hi(self):
        print("hi my name is",self.name)
p = Person("Nikhil")
p.say_hi()