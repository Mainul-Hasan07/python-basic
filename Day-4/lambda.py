

f = lambda a : a*a
print(f(10))

f = lambda a,b : a+b
print(f(7,9))

########
def is_even(n):
    return n%2==0
nums =[2,4,3,6,4,7,5]

evens = list(filter(is_even,nums))
print(evens)

evens = list(filter(lambda n : n%2==0,nums))
print(evens)

double = list(map(lambda n: n*2,evens))
print(double)

from functools import reduce 
sum = reduce(lambda a,b : a+b,double)
print(sum)


def div(a,b):
    return a/b

def smart_div(func):
    def inner(c,d):
        if(c<d):
            c,d = d,c
        return func(c,d)
    return inner

division = smart_div(div)
print(division)
result = division(3,6)
print(result)





def modulous(a,b):
    return a%b

def smart_modulous(func):
    def inner(c,d):
        if c<d:
            c,d = d,c
        return func(c,d)
    return inner

modulous1 = smart_modulous(modulous)
print(modulous1(47,4))
