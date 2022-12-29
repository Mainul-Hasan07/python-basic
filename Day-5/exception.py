a= 5
b = 2

try:
    print(a/b)
    k = int(input('Enter a number: '))
    print(k)
except ZeroDivisionError as e :
    print('Hey,Pls can not divided by Zero',e)
except ValueError as e:
    print('Invalid error')
except Exception as e:
    print("went wrong")

print("Bye")