class Bar():
    var1 = 150
    
    def __init__(self, param1=10, param2=20):
        self.var1 = param1
        self.var2 = param2
        
    def __repr__(self):
        return f"Var1:{self.var1} Var2:{self.var2} classVar:    {__class__.var1}"
    
    @classmethod
    def increment_class_variable(cls):
        cls.var1 += 1

obj3 = Bar(1,100)
obj4 = Bar()
print(obj3)#Var1:1 Var2:100 classVar:150
print(obj4)#Var1:10 Var2:20 classVar:150

obj3.var1 = 500
print(obj3)#Var1:500 Var2:100 classVar:150

Bar.increment_class_variable()
print(obj3)#Var1:500 Var2:100 classVar:151