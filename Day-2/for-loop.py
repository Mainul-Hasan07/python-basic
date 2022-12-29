# deal with sequence (list,tuple,range,set,string)
x = "navin"
for i in x :
    print(i)

for i in range(11,21,2):
    print(i)


for i in range(20,10,-1):
    if i % 5!= 0:
        print(i)

import math as m
for i in range(1,51):
    if m.sqrt(i)== int(m.sqrt(i)) and i != 1:
        print(i)
