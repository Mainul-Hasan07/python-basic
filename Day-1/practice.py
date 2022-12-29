details = {"name":'navin','age':24,'hobby':'programming','department':'cse'}
fruits = dict(mango='yellow',orange='light-yellow',apple='red',cherry='light-red')
device=dict([(1,'camera'),(2,'mobile'),(3,'laptop'),(4,'watch')])
print(details)
print(fruits)
print(device)

### Access Items ###
print(details['age'])
print(details.get('age'))

### ADD/CHANGE VALUE ###
details['age']=28
details['weight']=70
details.update({'height':'6ft'})
print(details)


### REMOVE ITEMS ###
details.pop('height')
print(details)
details.popitem()
print(details)

del details['department']
print(details)