#verificação de abordagem
'''def max_1(S):
    if len(S) == 1:
        print(S[0])
        return S[0]
    else:
        print(S.pop())
        max_1(S)

S = [1, 3, 5, 7]
max_1(S)'''

#primeira tentativa
def max_2(S, posicao, maior):

    if posicao == 3:
        if maior < S[posicao]:
            maior = S[posicao]
        return maior
    
    else:
        if maior < S[posicao + 1]:
            maior = S[posicao + 1]
        
        return max_2(S, posicao + 1, maior)
        


W = [9, 3, 10, 11]
print(max_2(W, 0, W[0]))
