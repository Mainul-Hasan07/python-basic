# Method Overloading => same method but different parameter / arguments

class Teacher:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a
        return s

s1 = Teacher(23,21)
print(s1.sum(1,3))


############ Method Overriding ###########
# Same class/inheritance ,same method ,same parameter/arguments
class A:
    def show(self):
        print('In A show')
class B(A):
    def show(self):
        print('In B show')

a1 = B()
a1.show()


###################### Abstract ####################
# Abstract method => it's declaration but not difinition.
# In another language,a class which contain abstract method that's called Abstract class.
# But Python,it's declare the abstract class and mention abstract method that time considered as Abstract class.
# Otherwise it's normal class.

from abc import ABC ,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass 

class Laptop(Computer):
    def process(self):
        print("it's running")


com1 = Laptop()
com1.process()