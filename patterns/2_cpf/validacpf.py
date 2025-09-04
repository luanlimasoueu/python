class ValidaCpf:
    def __init__ (self, cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf( self, cpf):
        self.cpf = cpf
        