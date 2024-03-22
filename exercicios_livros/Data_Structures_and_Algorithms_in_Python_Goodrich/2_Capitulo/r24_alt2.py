
 
    # Function to add an edge to the graph
def flower(flowers, name, petals, price ):
    flowers.append([name, petals, price])

def get_flower(flowers):
    for i in flowers:
        print(i)


if __name__ == '__main__':
 
    flowers = [] 

 
# Add edges to the graph
flower(flowers , "Gardênia", 1, 6)
flower(flowers , "Gardênia", 1, 6)
get_flower(flowers)
