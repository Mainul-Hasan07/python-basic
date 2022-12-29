av = 10

x = int (input('How many candies you want?'))

i = 1 
while i <= x:
    if i > av:
        print('Out of stock')
        break
    print('Candy',i)
    i += 1

list1 = []
for i in range(1,101):

    if i % 3 == 0 or i%5 ==0:
        continue
    list1.append(i)

print(list1)
print(len(list1))


for i in range(1,101):
    if(i%2!=0):
        pass

    else: 
        print(i,end=' ')


