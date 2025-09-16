# Definindo uma metaclasse
class UppercaseAttributes(type):
    def __new__(cls, name, bases, dct):
        uppercase_attrs = {
            key.upper() if not key.startswith("__") else key: value
            for key, value in dct.items()
        }
        return super().__new__(cls, name, bases, uppercase_attrs)

# Usando a metaclasse para criar uma classe
class MyClass(metaclass=UppercaseAttributes):
    foo = "bar"
    baz = 123

print(hasattr(MyClass, "foo"))  # False (foo virou FOO)
print(MyClass.FOO)             # bar
print(MyClass.BAZ)             # 123
