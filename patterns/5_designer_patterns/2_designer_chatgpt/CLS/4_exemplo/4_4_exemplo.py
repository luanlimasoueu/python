class Foo():
    variable1 = 10
    @classmethod
    def increment_class_variable(cls):
        cls.variable1 +=1
obj1 = Foo()
obj2 = Foo()
print(f'Variable1 for obj1 {obj1.variable1} Variable1 for obj2 {obj2.variable1}')
#Variable1 for obj1 10 Variable1 for obj2 10

obj2.variable1 =  obj2.variable1 + 500
print(f'Variable1 for obj1 {obj1.variable1} Variable1 for obj2 {obj2.variable1}')
#Variable1 for obj1 10 Variable1 for obj2 510

Foo.increment_class_variable()
print(f'Variable1 for obj1 {obj1.variable1} Variable1 for obj2 {obj2.variable1}')
#Variable1 for obj1 11 Variable1 for obj2 500