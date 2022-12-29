
class Student:
    def __init__(self,name,rollno) -> None:
        self.name = name 
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    class Laptop:
        def __init__(self) -> None:
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = '8GB'
        def show(self):
            print(self.brand,self.cpu,self.ram)


s1 = Student('Navin',10)
s2 = Student('Rahim',13)
s1.show()
s2.show()
s1 = Student.Laptop()
print(s1.brand)