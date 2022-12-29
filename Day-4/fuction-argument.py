def update(x):
    x = 8
    print('x: ',x)

a = 10
update(a)
print('a: ',a)

############## TYPES ##################
# Two types 
# 1.Formal Agrument
# 2.Actual Argument- it's 4 types
#    a.Position
#    b.Keyword
#    c.Default
#    d.Variable Length

def add(a,b):
    c = a + b
    print(c)

add(21,23)

# a. Position
def person(name,age=18):
    print(name)
    print(age)

person('navin',24)

# b. Keyword
person(age=23,name='navin')

# c. Default
person('navin',28)

# Variable-length
def sum(a, *b):
    c = a
    for i in b:
        c = c+ i
    print(c)

sum(5,6,2,3,6,4)

def person(name,**data):
    print(name)
    print(data.items())
    for i,j in data.items():
        print(i,j)

person('navin',age=34,city='Mumbai',mobile=43567)
