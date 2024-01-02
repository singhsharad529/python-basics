

# iterative method
def fibonachhiPrint(n,a,b):
    if(n==1):
        print(a,end=" ")
        return

    print(a,b,end=" ")
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(c,end=" ")


# recursion approach: nth fibonachhi
def fibonachiRec(n):
    if(n==1):
        return 0
    if(n==2):
        return 1

    result=int(fibonachiRec(n-2))+int(fibonachiRec(n-1))
    return result

a=0
b=1

n=int(input("Enter nth number for fibonaachi series\n"))

# fibonachhiPrint(n,a,b)
result =fibonachiRec(n)
print('result',result)
