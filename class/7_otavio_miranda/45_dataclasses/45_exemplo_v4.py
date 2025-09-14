from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    lastname: str
    active: bool = False
    addresses : list = field( 
        default_factory = list,
        repr= False,
        compare=True,
        kw_only= True
        )
    full_name: str = field( 
        default = 'Missing', 
        init = False,
        repr= False
        )
    
    def __post_init__( self):
        self.full_name = f'{self.name}'\
        f'{self.lastname}'
    
    
if __name__ == '__main__':
    john1 = Person('John', 'Doe', True, addresses=['R1'])
    john2 = Person('John', 'Doe', True, addresses= ['R2'])
    mary = Person('Mary', 'Jane')
    print(john1 == john2  )