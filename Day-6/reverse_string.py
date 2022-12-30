n = 'mainul'
m = ''
for i in n:
    m = i+ m

print(m)

from datetime import date
 
def CalculateAge(birthDate):
    today = date.today()
    year = today.year - birthDate.year 
    month = today.month - birthDate.month
    day = today.day - birthDate.day
    age = date(year,month,day)
    return year,month,day

print(CalculateAge(date(1999,7,8)))