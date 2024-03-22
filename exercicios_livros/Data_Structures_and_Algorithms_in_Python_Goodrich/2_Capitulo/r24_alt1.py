
 
class Flowers:
    def __init__(self):
        self.flowers = []
 
    # Function to add an edge to the graph
    def flower(self, name, petals, price ):
        self.flowers = self.flowers
        self.flowers.append([name, petals, price])


    def get_flower(self):
        for i in self.flowers:
            print(i)


# Create a graph
graph = Flowers()
 
# Add edges to the graph
graph.flower("Gardênia", 1, 6)

graph.get_flower()

graph.flower("Girassol", 2, 6)

graph.get_flower()