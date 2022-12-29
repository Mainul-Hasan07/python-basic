
class Computer:

    def __init__(self,cpu,ram) :
        self.cpu=cpu
        self.ram = ram

    def config(self):
        print('Config is',self.cpu,self.ram)

com1= Computer('i5',16)
com2 = Computer('Ryzen 3',8)

Computer.config(com1)
com1.config()
com2.config()


class Student:

    def __init__(self,id,gpa) -> None:
        self.id = id
        self.gpa = gpa

    def result(self):
        print(f"{self.id} {self.gpa}")

Rahim = Student(101,4.5)
karim =Student(102,4.78)

Rahim.result()
Student.result(karim)


########################################
# 1. Every object allocate new space
# 2. size of object depends on no. of variable
# 3. Constructor allocates size of object

class Details:
    def __init__(self) -> None:
        self.age= 30
        self.weight = 5.8
    def compare(self,other):
        if person1.age == person2.age:
            return True
        else: 
            return False 

person1 = Details()
person1.age= 32
person2 = Details()

if person1.compare(person2):
    print("Ther are same")
else:
    print("They are different")