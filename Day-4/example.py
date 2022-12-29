
def count(lst):
    even= 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even+=1
        else:
            odd+=1
    return even,odd


n = int(input('Enter number of list: '))
lst=[]
for i in range(n):
    x = int(input('Enter next value: '))
    lst.append(x)
print(lst)
even,odd = count(lst)
print("Even : {} and Odd : {}".format(even,odd))



#####################################3

def countName(names):
    count =0
    lst1= []
    for i in names:
        if len(i) >= 5:
            count+=1
            lst1.append(i)
    return count,lst1

lst =[]
for i in range(10):
    name = input('Enter 10 names: ')
    lst.append(name)
result,names = countName(lst)
print(result,names)

