class var:
    a=10
    b=20
    def dis(self):
        print(self.a+self.b)

t=var()
t.dis()


###############

class ObjectLocation:
    def display(self):
        pass

ob1=ObjectLocation()
ob2=ObjectLocation()
ob3=ob1
print(id(ob1))
print(id(ob2))
print(id(ob3))
print(id(ob1)==id(ob3))#True