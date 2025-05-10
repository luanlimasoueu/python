class User(object):
    """Uma classe bem simples.
    """
    def __init__(self, name):
        """Inicializa a classe, atribuindo um nome
        """
        self.name = name
# Um novo método para a classe
def set_password(self, password):
    """Troca a senha
    """
    self.password = password
print ('Classe original:', dir(User))
# O novo método é inserido na classe
User.set_password = set_password
print ('Classe modificada:', dir(User))
user = User('guest')
user.set_password('guest')
print ('Objeto:', dir(user))
print ('Senha:', user.password)