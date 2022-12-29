from threading import *
from time import *
class Hello(Thread) :
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(.1)

class Hi(Thread) :
    def run(self):
        for i in range(5):
            print("HI")
            sleep(.1)

obj1 = Hello()
obj2 = Hi()

obj1.start()
sleep(.01)
obj2.start()

obj1.join()
obj2.join()

print('Bye')
