pos = -1

def search(lst,n):
    l = 0
    u = len(lst)-1 

    while l <= u:
        mid = (l+u)//2
        if lst[mid] == n:
            global pos
            pos = mid+1
            return True
        else:
            if lst[mid] < n:
                l = mid+1
            else: 
                u = mid-1




lst = sorted([2,4,6,3,8,5,9,7])
print(lst)
n = 7

if search(lst,n):
    print("Found",pos)
else: 
    print("Not Found") 