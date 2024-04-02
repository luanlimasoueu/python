def transfer(S, T):
    if len(S) == 0:
        return S, T
    else:
        T.append(S.pop())
        return transfer(S, T)
    
print(transfer([1,3], []))


