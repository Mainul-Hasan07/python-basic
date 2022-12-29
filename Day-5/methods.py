# Types 
# 1. Instance Methods
#       a. Accessor methods
#       b.Mutator methods
# 2. Class Methods
# 3. Static Methods => method which can not concernd with class/instance variables

class Student:

    school = "Telusko"

    def __init__(self,m1,m2,m3) -> None:
        self.m1 =m1
        self.m2=m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # Accessor methods => fetch instance variable
    def get_M1(self):
        return self.m1

    # Mutator methods => modify instance variables
    def set_M1(self,value):
        self.m1 = value

    # Class methods => work with class variables
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static methods
    def info():
        print(" ")


s1 = Student(34,54,57)
s2 = Student(65,46,86)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())