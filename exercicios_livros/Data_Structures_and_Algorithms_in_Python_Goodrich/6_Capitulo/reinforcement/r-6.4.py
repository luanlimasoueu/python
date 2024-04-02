def rev(S):
    if len(S) == 0:
        return 1
    else:
        S.pop()
        print(S)
        return rev(S)
    
S = [4,3,5,6]
rev(S)

