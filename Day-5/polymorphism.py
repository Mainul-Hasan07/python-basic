
class pyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()


ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)

############ OPerator Overloading ##############333

a = 5
b = 6
print(a+b)

print(int.__add__(a,b))

class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2
    def __add__(self,x):
        m1 = self.m1 +x.m1 
        m2 = self.m2 + x.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self,x):
        r1 = self.m1+ self.m2
        r2 = x.m1 + x.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self) -> str:
        return "{} {}".format( self.m1,self.m2)

s1 = Student(23,43)
s2 = Student(22,54)
s3 = s1 + s2
print(s3.m1,s3.m2)

if s1 > s2:
    print("a1 wins")
else:
    print("a2 wins")

print(s1)