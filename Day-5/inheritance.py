# Inheritance 
class A:
    def feature1():
        print('Feautre 1 working')
    def feature2():
        print('Feautre 2 working')

# Single level Inheritance

class B(A):
    def feature3():
        print('Feautre 3 working')
    def feature4():
        print('Feautre 4 working')

# Multi level Inheritace

class C(B):
    def feature5():
        print('Feature 5 working')


class D:
    def feature6():
        print('Feature 6 working')

# Multiple Inheritance
 
class E(A,D):
    def feature7():
        print('Feature 7 working')

s1 = E()
