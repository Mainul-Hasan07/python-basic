pos = 0
def search(lst,n):
    for i in range(len(lst)):
        if lst[i] == n:
            global pos
            pos = i+1
            return True
    return False


def search1(lst,n):
    i = 0
    while i< len(lst):
        if lst[i] == n:
            global pos
            pos = i+1
            return True
        i +=1
    return False


lst = sorted([2,4,6,3,8,5,9,7])
print(lst)
n = 9

if search1(lst,n):
    print("Found",pos)
else: 
    print("Not Found")