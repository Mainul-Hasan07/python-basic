f = open("MyData",'w')
f.write("My name is Mainul.\nI'm from Bogura")

f1 = open('pic3.jpg','rb')             # rb = read binary
f2 = open('myPic.jpg','wb')             # wb = write binary
for i in f1:
    f2.write(i)