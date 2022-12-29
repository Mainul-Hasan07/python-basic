# 6 way to create Array
# 1.array()
# 2.linspace()
# 3.logspace()
# 4.arange()
# 5.zeros()
# 6.ones()


from numpy import *
arr = array([1,2,3,4,5])
arr2 = array([1,2,3,4,5],float)
print(arr)
print(arr2)
print(arr.dtype)
print(arr2.dtype)


##################
arr = linspace(0,9,10)
print(arr)

######################
arr = arange(0,15,2)
print(arr)


##########################
arr = logspace(1,40,10)
print('%.2f' %arr[4])

###########################
arr = zeros(10)
print(arr)

arr = ones(5)
print(arr)