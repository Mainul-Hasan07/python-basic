from numpy import *
arr1 = array([
                [1,2,3,4],
                [9,7,8,6]
                ])

print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape,arr1.size)

arr2 = arr1.flatten()
print(arr2)

arr3 = array([
                [1,2,3,4,5,6],
                [4,5,6,3,7,6]
])

arr4 = arr3.reshape(2,2,3)
print(arr4)
print(arr4.dtype)
print(arr4.ndim)
print(arr4.shape,arr4.size)

####################### Matrices ########################
m1 = matrix('1 2 3;4 5 6;9 8 7')
m2 = matrix('2 3 1;4 6 4;4 3 4')
print(m1)
print(diagonal(m1))
print(m1.min())
print(m1.max())

mul1 = m1 * m2
sum1 = m1 + m2
print(mul1)
print(sum1)

m = matrix('1,2,3;2,3,4;5,6,1')
m1 = matrix([[9,3,2],[23,21,0],[-4,-1,-7]
])
print(m1)
print(m)

muls = m * m1
print(muls)

add = m+m1
print(add)
print(diagonal(m))
print(diagonal(m1))
print(m.max())
print(m.min())