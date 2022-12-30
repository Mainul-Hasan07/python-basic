a = 5 
b= 10

temp = a
a = b
b = temp
print(a,b)

a , b = b,a
print(a,b)

a = a+ b
b = a -b
a = a - b
print(a,b)

a = a^b  # Subtraction
b = a^b
a = a^b
print(a,b)


############# Greatest Common divisor ###########
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

def GCD(a,b):
    if a> b:
        smaller = b
    else: 
        smaller = a
    for i in range(1,smaller+1):
        if a%i ==0 and b%i ==0:
            gcd = i
    return gcd

result = GCD(a,b)
print(result)


################## Smallest Number ##############
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def MIN(a,b,c):
    if a<b and a<c:
        smallest = a
    elif b<c:
        smallest = b
    else:
        smallest = c
    return smallest

result = MIN(a,b,c)
print(result)

#################### Largest Number #################
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))

def MAX(a,b,c):
    if a>b and a>c:
        max = a
    elif b>c:
        max = b
    else:
        max = c
    return max

result = MAX(a,b,c)
print(result)
