x = input("Enter 1st number: ")
y = input("Enter 2nd number: ")
#print(type(x),type(y))
z = int(x)+ int(y)
print("Your result: ",z)

ch = input('enter a char: ')
print(ch[0].upper())

result = eval(input('enter a expression: '))
print(result)


########### Passing value from Command ################
import sys
a= sys.argv[1]
b = sys.argv[2]
c = int(a)+int(b)
print(c)