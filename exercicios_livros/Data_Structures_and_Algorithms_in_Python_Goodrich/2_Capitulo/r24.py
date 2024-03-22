class Flower:

    def __init__(self, name, petals, price ):
        self.name = name
        self.petals = petals
        self.price = price
    
    def get_name(self):
        print( "O nome da flor é: " , self.name)

    def get_petals(self):
        print( "A quantidade de pétalas é: " , self.name)
    
    def get_price(self):
        print( "O preço é: " , self.price)



if __name__ == '__main__':

    flowers = [ ]    

    flowers.append(Flower('girassol', 1, 5) )  

    for i in range(len(flowers)):
        flowers[i].get_name()
        flowers[i].get_petals()
        flowers[i].get_price()

    