def greet():
    print("Hello")
    print('Good Morning')

greet()

def addTwo(n1,n2):
    s = n1 + n2
    return(s)
print(addTwo(10,20))
print(addTwo(999833,373947298))


def add_sub(n1,n2):
    c =n1+n2
    d =n1-n2
    return c,d
result1,result2 = add_sub(39,21)
print(result1,result2)