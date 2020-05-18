class human:
    def __init__(self , name):
        self.name = name
        print("let's see what happens")
    def hello(self):
        print(self.name)

    

class Person(human):
    def __init__(self , name , key):
        super().__init__(name)                 #you can comment this out and not call the class human
        print("does this run")                 #just declare self.name and human does not run 
        self.key = key                         
    def vital_info(self):
        print("in second func")
        print(self.key)

person = Person("Doom" , "Betrayal")
Human = human("moneypenny")
person.hello()
person.vital_info()

Human.hello()

print(f"is Person subclass of human ? Answer is :\n{issubclass(Person,human)}")
