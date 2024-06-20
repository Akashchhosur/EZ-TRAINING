n=int(input("enter the number:"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
fact(n)
print(fact(n))

'''
input: 
enter the number:5

output:120   '''
