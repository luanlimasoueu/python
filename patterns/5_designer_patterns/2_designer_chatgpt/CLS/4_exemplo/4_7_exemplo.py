class Bar():
    table1 = [10,20]
    table2 = [1,1,1]
    def __init__(self, param1): 
        self.table1 = param1
    def append_class_table(self, value):
        __class__.table1.append(value)
    @classmethod  
    def append_class_table_with_cls(cls, value): 
        cls.table1.append(value)
    def __repr__(self):
        return f'class table1:{__class__.table1} class table2:{__class__.table2} instance table1:{self.table1}'
    
table = [11,12,13,14,15]
obj1 = Bar([3,4,5])
obj2 = Bar([40,50,60])
print(obj1)#class table1:[10, 20] class table2:[1, 1, 1] instance table1:[3, 4, 5]
print(obj2)#class table1:[10, 20] class table2:[1, 1, 1] instance table1:[40, 50, 60]

print()
obj2.append_class_table(50)
obj1.append_class_table_with_cls(60)
print(obj1)#class table1:[10, 20, 50, 60] class table2:[1, 1, 1]    instance table1:[3, 4, 5, 10]
print(obj2)#class table1:[10, 20, 50, 60] class table2:[1, 1, 1]    instance table1:[40, 50, 60]

print()
obj1.table1.append(10)
print(obj1)#class table1:[10, 20] class table2:[1, 1, 1]    instance table1:[3, 4, 5, 10]
print(obj2)#class table1:[10, 20] class table2:[1, 1, 1]    instance table1:[40, 50, 60]

print()
obj2.table2[1] = 10
print(obj1)#class table1:[10, 20, 50] class table2:[1, 10, 1]    instance table1:[3, 4, 5, 10]
print(obj2)#class table1:[10, 20, 50] class table2:[1, 10, 1]    instance table1:[40, 50, 60]

print()
obj2.table2 = table
print(obj1)#class table1:[10, 20, 50] class table2:[1, 10, 1]    instance table1:[3, 4, 5, 10]
print(obj2)#class table1:[10, 20, 50] class table2:[1, 10, 1]    instance table1:[40, 50, 60]

