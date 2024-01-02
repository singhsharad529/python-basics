
def findFact(n):
    if(n==1 or n==2):
        return n

    return n*findFact(n-1)

n=int(input("Enter number to get factorial\n"))

result=findFact(n)
print(result)