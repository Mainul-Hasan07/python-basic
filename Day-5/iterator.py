class TopTen:
    def  __init__(self,num) -> None:
        self.num = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 100:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values= TopTen(50)
#print(next(values))

for i in values:
    print(i)


nums =[3,2,5,7,3]
it = iter(nums)
print(next(it)) 