class Foo():
    variable1 = 10
    variable2 = 'Some class variable string'
    
    @classmethod
    def increment_class_variable(cls):
        cls.variable1 +=1

Foo.increment_class_variable()
print(Foo.variable1) #prints 11