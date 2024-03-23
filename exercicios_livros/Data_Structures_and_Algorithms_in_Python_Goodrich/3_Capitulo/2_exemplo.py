def binary_search(data, target, low, high):

    if low > high:
        return False    
    else:
        mid = (low + high) // 2
        if target == data[mid]: 
            print(target)
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)
        

numero = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

binary_search(numero, 18, 0, 10)