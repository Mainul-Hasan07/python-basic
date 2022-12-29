num = 39

for i in range(2,num):
    if num % i == 0:
        print('Not prime due to divided by',i)
        break
else:
    print('prime')

from math import sqrt
if num>1:
    for i in range(2,int(sqrt(num))+ 1):
        if num % i == 0:
            print(num,'is not prime number')
            break
    else:
        print(num,'is prime number')

prime = []
nPrime = []
for num in range(100):
    if num>1:
        for i in range(2,int(sqrt(num))+1):
            if num % i ==0:
                nPrime.append(num)
                break
        else:
            prime.append(num)
print(prime)
print(len(prime))
print(nPrime,len(nPrime))