x = 11
r = x%2
if r==0:
    print('even')
    if(x>5):
        print("Great")
    else:
        print('not so Great')
else:
    print('odd')



a= 2
if(a==1):
    print('one')
elif(a==2):
    print('two')
elif(a==3):
    print('Three')
elif(a==4):
    print('Four')

else:
    print('wrong input')



a=2
b= 330
print('A') if a>b else print('B')

a=330
b=330
print('A') if a>b else print("=") if a==b else print('B')