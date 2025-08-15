class Foo():
    variable1 = 10

    @classmethod
    def increment_class_variable(cls):
        cls.variable1 +=1

    @classmethod
    def print_var1(cls):
        print(cls.variable1)

obj1 = Foo()
obj2 = Foo()
obj2.variable1 = 500
Foo.increment_class_variable()
obj2.print_var1() #prints 11
print(obj2.variable1) #prints 500