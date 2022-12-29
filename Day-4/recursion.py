import sys
sys.setrecursionlimit(5)
print(sys.getrecursionlimit())
i=0
def greet ():
    global i
    i +=1
    print('Hello',i)
    greet()
greet()


############## FACTORIAL ####################

def factorialNum(n):
    f = n* (n-1)
    return factorialNum(n-1)
print(factorialNum(5))