from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([3,2,5,7,4])
arr = arr1 + arr2

print(arr)
print(sin(arr1))
print(sqrt(arr))
print(sum(arr))
print(concatenate([arr1,arr2]))

list1 = list([1,2,3])
list2 = list([6,4,3])
list3 = list1 + list2
print(list3)


############# COPY #################
# SHALLOW COPY(.view()) - When change values of array ,copying array can be change
# DEEP COPY(.copy()) -  When change values of array ,copying array can not be change
arr1 = array([1,2,3,4,5,6,7,8])
arr2 = arr1.view()
arr3 = arr1.copy()
arr1[4]=10

print(arr2)

print(id(arr1))
print(id(arr2))


print(arr3)
print(id(arr3))

#########################################

arr1 = array([2,5,3,7])
arr2 = array([9,8,7,6])

arr =array([])
for i in range(len(arr1)):
    x = arr1[i] + arr2[i]
    arr = append(arr,x)

print(arr)


lgValue = 0
for i in range(len(arr2)):
    if(arr2[i]>lgValue):
        lgValue = arr2[i]
print(lgValue)