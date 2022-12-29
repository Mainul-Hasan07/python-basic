def fib(n):
    a=0
    b=1
    if n>0:
        if n==1:
            print(a)
        else:
            print(a)
            print(b)
        for i in range(2,n):
            c =a+b
            a=b
            b=c
            print(c)
    else:
        print("Please enter positive Number")
fib(10)



def fiboSeries(n):
    fibo = [0,1]
    for i in range(2,n):
        c=fibo[i-1]+fibo[i-2]
        fibo.append(c)
    return fibo
print(fiboSeries(100))