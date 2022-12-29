details={'name':'navim','age':35,'weight':70,'height':"6ft"}
# Change Values #
details['age']=25
details.update({'age':27})

print(details)
print("Number:",len(details))

age= details.get('age')
details.pop('height')
details.update({'hobby':'programming'})

# Get key#
print(details.keys())
# GEt Items #
print(details.items())
print(details)
print(age)

# GEt value #
print((details.values()))


bio = dict(name="mainul",age=35)
print(bio)


keys= {'navin','kiran','harsh'}
values={'python','java','js'}
data=dict(zip(keys,values))
print(data)

# Access items #
person1=data['kiran']
print(person1)
print(data.get('kiran'))


# ###############
prog= {'JS':'Atom','cs':'VS','Python':['Pycharm','Sublime'],'Java':{'JSE':'Netbeans','JEE':'Eclipse'}}
print(prog['JS'])
print(prog['Python'][1])
print(prog['Java']['JEE'])


