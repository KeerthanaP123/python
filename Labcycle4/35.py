class time():
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self, other):
        return "Time is:"+str(self.__hour+other.__hour)+":"+str(self.__minute+other.__minute)+":"+str(self.__second+other.__second)
print("Time 1")
h1=int(input("Enter hour in time 1:"))
m1 = int(input("Enter hour in time 1:"))
s1 = int(input("Enter minute in time 1:"))
print("Time 2")
h2 = int(input("Enter second in time 1:"))
m2 = int(input("Enter hour in time 2:"))
s2 = int(input("Enter hour in time 2:"))
t1=time(h1,m1,s1)
t2=time(h2,m2,s2)
print(t1+t2)
class Time():
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
    def __add__(self, other):
        sum1=self.__hour+other.__hour
        sum2=self.__minute+other.__minute
        sum3=self.__second+other.__second
        if sum3>=60:
            sum3=sum3-60
            sum2=sum2+1
        if sum2>=60:
            sum2=sum2-60
            sum1=sum1+1
        print(sum1,":",sum2,":",sum3)
print("Time 1")
h1=int(input("Enter hour in time 1:"))
m1=int(input("Enter minute in time 1:"))
s1=int(input("Enter second in time 1:"))
print("Time 2:")
h2=int(input("Enter hour in time 2:"))
m2=int(input("Enter minute in time 2:"))
s2=int(input("enter second in time 2:"))
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
t1+t2