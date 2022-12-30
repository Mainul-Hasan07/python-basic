
def lst(value):
    lst =[]
    for i in range(len(value)):
        num = int(value[i])
        lst.append(num)
    return lst

def sort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i,len(nums)):
            if nums[j]<nums[minpos]:
                minpos = j
        nums[minpos],nums[i] = nums[i],nums[minpos]
    return nums

def RemoveDuplicate(num):
    result = []
    for i in num:
        if i not in result:
            result.append(i)
    return result  

value = list(input("Enter series of number: "))
value1 = list(input("Enter series of number: "))
nums1 = lst(value)
nums2 = lst(value1)
result1 = sort(nums1)
result2 = sort(nums2)
print(result1,result2)
nums3 = (result1+result2)

result = RemoveDuplicate(nums3)
print(sort(result))



