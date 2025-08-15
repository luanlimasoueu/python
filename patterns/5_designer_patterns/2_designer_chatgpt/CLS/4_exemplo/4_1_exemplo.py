class Foo:
    variable1 = 10
    variable2 = 'Some class variable string'

obj1 = Foo()
obj2 = Foo()

print(f'class_integer for obj1 {obj1.variable1}') # class_integer for obj1 10
print(f'class_integer for obj2 {obj2.variable1}') # class_integer for obj2 10

Foo.class_integer = 100

print(f'class_integer for obj1 {obj1.variable1}') # class_integer for obj1 100
print(f'class_integer for obj2 {obj2.variable1}') # class_integer for obj2 100    