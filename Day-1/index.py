# Global variable
x = "python is "
def myfunc():
    print(x + "awesome")

myfunc()
print(x+"Awesome")


# Local variable
def agefunc():
    global age
    age = str(14)
    print("I am "+age+" years old")

agefunc()
print("I am",age,"years old")

# Global variable to change value
color= 'white'
def colorFunc():
    global color
    color="Black"
    print("memorable "+color)

colorFunc()
print("Uffs, its",color)