class rectangle():
    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    def area(self):
        return self.length*self.bredth
a=int(input("Enter bredth 1 of rectangle:"))
b=int(input("Enter height of 1 rectangle:"))
obj=rectangle(a,b)
print("Area of rectangle",obj.area())
c=int(input("Enter bredth of 2 rectangle:"))
d=int(input("Enter height of 2 rectangle:"))
obj2=rectangle(c,d)
print("Area of 2 rectangle",obj2.area())
if(obj.area()==obj2.area()):
    print("Area of 2 rectangle are equal")
else:
    print("Area of 2 rectangle are not equal")