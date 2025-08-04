#1. Singleton com @decorator

def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance

@singleton
class Config:
    def __init__(self):
        self.valor = 42

a = Config()
b = Config()

print(a is b)         # True
print(a.valor)        # 42
b.valor = 100
print(a.valor)        # 100 (mesma instância)
