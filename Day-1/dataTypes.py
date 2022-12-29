# Types
# 1.None - like null which use others language
# 2.Numeric - int,float,complex,bool
# 3.List-
# 4.Tuple
# 5.Dictonaries 
# 6.Set
# 7.Range
# 8.String

# Converting data types
a= 2.9
b = int(a)
print(type(a))
print(b)
print(type(b))

k= float(a+b)
print(k)
print(type(k))

c = complex(b,int(k))
print(c,type(c))

print(b<k)
print(int(True))
print(int(False))


#########  Sequence ##########
list1= [12,13,14,15,15,16,34,54,76]
set1 = {23,32,43,54,32,53,'navin'}
tuple1 = (23,23,43,54,23,53)
string = 'mainul'
 
print(type(list1))
print(type(set1))
print(type(tuple1))
print(type(string))

#### Range ####
list2 =list(range(10)) 
print(list2)
list3 = list(range(1,10,2))
print(list3)

####### Dictionary #########
d = {'navin':'samsung','rahul':'iphone','kiran':'oneplus'}
print(d)
print(d.keys())
print(d['kiran'])
print(d.get('kiran'))

