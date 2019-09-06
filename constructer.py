
'''class contructer:

    def display(self):
        print("Inside method")

    def __init__(self):
        print("Inside consuster")

c1=contructer()
c1.display()#Inside consuster # Inside method'''


###############################
'''class contructer:

    def display(self,a,b):
        print(a)
        print(b)
        self.a=a
        self.b=b


    def display1(self):
        print(self.a*self.b)

c=contructer()
c.display(10,20) #10 #20
c.display1()#200


############################### Using constructor above program############


class contructer:

    def __init__(self,a,b):
        print(a)
        print(b)
        self.a=a
        self.b=b


    def display1(self):
        print(self.a*self.b)#10#20

c=contructer(10,20)
c.display1()#200


##################calling one method from another method


class construct:
    def display(self):
        print("first method")
        self.display1(100)

    def display1(self,a):
        print("second method",a)


c=construct()
c.display1()


################

class Emp:
    def __init__(self,id,name,sex):
      self.id=id
      self.name=name
      self.sex=sex
    def display(self):
        print("Empid:{} Empname:{} Empsex:{}".format(self.id,self.name,self.sex))

c1=Emp()
c1.display(10,'lucky','male')'''


###########__if we want to print the object refernece

class Object:
 pass

c=Object()
print(c) #<__main__.Object object at 0x0148AD30>






###########__str__ used to give meaningful representation of object


class Object:
 def __str__(self):
     return "welcome"



c=Object()
print(c)#welcome


################


class Emp:
    def __init__(self,id,name,sex):
      self.id=id
      self.name=name
      self.sex=sex
    def __str__(self):
        return ("Empid:{} Empname:{} Empsex:{}".format(self.id,self.name,self.sex))

c1=Emp(10,'lucky','male')
print(c1)


########Destory the objects

class object:
    def __del__(self):
        print("destory")

c1=object()
c2=object()

del c1