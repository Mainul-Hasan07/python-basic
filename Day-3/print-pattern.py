for j in range(4):
    print('# ',end="")

print() # Create a new line

for j in range(4):
    print('#',end=' ')

print()

for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()


for i in range(4):
    for j in range(i+1):
        print('# ',end='')
    print()


for i in range(4):
    for j in range (4-i):
        print('# ',end='')
    print()


s = 8
for i in range(s):
    for j in range(s):
        if ((i==0 or (i==s-1 and j <= s//2)) or j==4):
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()
    
s = 8
for i in range(s):
    for j in range(s):
        if (i==0 or i==s-1 or i==s//2 or j==0):
            print('* ',end='')
        else:
            print(' ',end=' ')
    print()


for i in range(4):
    for j in range(4-i):
        if(i==0):
            x= j+1
            print(x,end=' ')
        elif(i==1):
            x= j+2
            print(x,end=' ')
        elif(i==2):
            x= j+3
            print(x,end=' ')
        else:
            x= j+4
            print(x,end=' ')
    print()


for i in range(4):
    for j in range(4-i):
        print(i+j+1,end=" ")
    print()