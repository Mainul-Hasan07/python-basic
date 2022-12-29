def factNum(n):
    f=1
    for i in range(1,n+1):
        f = f*i
    return (f)

print(factNum(10))


############## FACTORIAL ####################

def factorialNum(n):
    if n==0:
        return 1
    return n*factorialNum(n-1)

print(factorialNum(10))

def fib(n):
    fibo = [0,1]
    for i in range(2,n):
        c = fibo[i-2 ]+fibo[i-1]
        fibo.append(c)
    return fibo
print(fib(10))