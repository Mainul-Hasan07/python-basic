# Types 
# 1. Instance => instance namespace(area where create an object/variable)
# 2. Static(Class) => class namespace


class car:

    wheels = 4  # Static(class) variable

    # Instance Variable
    def __init__(self) -> None:
        self.mil = 10
        self.com = "BMW"

c1 = car()
c2 = car()
c1.mil = 6
car.wheels = 6
print(c1.mil,c1.com,c1.wheels)
print(c2.mil,c2.com,c2.wheels)