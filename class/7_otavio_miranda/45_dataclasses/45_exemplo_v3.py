class Person:
    
    def __init__( self, name, lastname):
        self.name = name
        self.lastname =  lastname
    
    def __str__ (self):
        class_str = f'{self.__class__.__name__}'\
        f'({self.name} {self.lastname})'
        return class_str
    
    def __repr__(self):
        return str(self)
    
    def __eq__( self, o):
        return self.lastname == o.lastname
    
if __name__ == '__main__':
    john1 = Person('John', 'Doe')
    john2 = Person('John', 'Doe')
    mary = Person('Mary', 'Jane')
    print(john1 == john2  )