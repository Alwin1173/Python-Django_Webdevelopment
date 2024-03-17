n=int(input("Enter no.:"))
def fact(n):
    x=1
    while(n!=0):
        x=x*n
        n=n-1
    print(x)
fact(n)
