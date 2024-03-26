def reverse(S, start, stop):
    if start < stop -1:
        print(S[start], S[stop])
        S[start], S[stop-1] = S[stop-1], S[start] 
        reverse(S, start+1, stop-1)

S = [4, 3, 6, 2, 8, 9, 5]
start = 0
stop = 6
reverse(S, start, stop)
