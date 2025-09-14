from dataclasses import dataclass, field

@dataclass
class Person( frozen= True, kw_only = True):
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
        full_name = f'{self.name}'\
        f'{self.lastname}'
        object.__setattr__(
            self,
            'full_name',
            full_name
        )
    
    
if __name__ == '__main__':
    john1 = Person(
        name ='John', lastname='Doe', 
        active= True, addresses=['R1'])
    john2 = Person(
        name ='John', lastname='Doe', 
        active= True, addresses= ['R2'])
    print(john1.__dict__)