
def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]


nums = [3,5,8,6,7]
sort(nums)
print(nums)





def sort1(nums):
    for i in range(len(nums)):
        minpos = i
        j = i
        while j <= (len(nums)-1):
            if nums[j] < nums[minpos]:
                minpos = j
            j+=1
        nums[i],nums[minpos]=nums[minpos],nums[i]
        print(nums)





nums = [5,3,8,6,7,2]
sort1(nums)
print(nums)