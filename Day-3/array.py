from array import *

vals = array('i',[3,4,22,64,32,32])

print(vals,vals.buffer_info())
print(vals.pop())

newArr = array(vals.typecode,(a*a for a in vals))
print(newArr)

for i in vals:
    print(i)

for i in range(len(vals)):
    print(vals[i])

vals = array('u',['a','e','i','o','u'])
vals.remove('a')
print(vals.tolist())


############## create array from User ################
arr = array('i',[])

n = int(input('Enter the length of the array'))

for i in range(n):
    x = int(input('Enter the next value'))
    arr.append(x)

print(arr)

######## From List ##############
list1 = [1,2,3,4,5,6,7,8,9]
vals = array("i",[])
vals.fromlist(list1)
print(vals.count(9))


########### search ##################
val = int(input('Enter the value for search'))
k=0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

print(arr.index(val))

n = int(input('Enter length of array :'))

nums = array('i',[])
for i in range(n):
    x= int(input('Ente the next value :'))
    nums.append(x)
print(nums)

for i in range(len(nums)):
    if i == 2:
        nums.remove(nums[2])
print(nums)


############ Reverse ####################
num2 = array('i',[])
for i in range(len(nums)-1,-1,-1):
    
    num = nums[i]
    num2.append(num)
    x-=1
print(num2)
