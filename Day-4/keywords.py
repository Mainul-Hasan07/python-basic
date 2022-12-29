a = 10

def something():
    a = 15
    print(a)
something()
print(a)


##### local variable convert to Global variable  ###
a = 10 
def nums():
    global a
    a = 20 
    print(a)
nums()
print(a)


####### Use local variable and Global variable in same time
a = 20 
b =10

def num():
    a= 5
    x= globals()['a']
    print(id(x))
    print(a,x)
num()
print(id(a))