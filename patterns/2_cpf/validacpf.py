import re

class ValidaCpf:

    def __init__(self, cpf):
        self.cpf = cpf  # chama o setter
        print(f"CPF recebido: {self.cpf}")
    
    def valida(self):
        if not self.cpf:
            return False
        
        # calcula os dois dígitos e compara com o cpf original
        novo_cpf = self.__calcula_digitos(self.cpf[:9])
        novo_cpf = self.__calcula_digitos(novo_cpf, digito=True)
        
        return novo_cpf == self.cpf
    
    @staticmethod
    def __calcula_digitos(fatia_cpf, digito=False):
        """Calcula o primeiro ou segundo dígito do CPF"""
        if not digito:
            multiplicadores = list(range(10, 1, -1))
        else:
            multiplicadores = list(range(11, 1, -1))

        soma = sum(int(n) * m for n, m in zip(fatia_cpf, multiplicadores))
        digito_gerado = (soma * 10) % 11
        digito_gerado = digito_gerado if digito_gerado <= 9 else 0
        
        return fatia_cpf + str(digito_gerado)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        # remove tudo que não seja número
        cpf = re.sub(r'[^0-9]', '', cpf)
        self._cpf = cpf
