def power(N, P):
    if P == 0:
        return 1
    else:
        return (N*power(N, P-1))
print(power(4, 2))


'''
input: 
5

output:
25'''