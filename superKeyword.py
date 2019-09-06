class super:
    a,b=10,20

    def display(self):
        print("parent class")

class child(super):
    c,d=50,60
    def display1(self):
        print(super().a,super().b)#super varibale#10 20
        print(self.c,self.d)#50 60
        super().display()# parent class

c=child()
c.display1()


#Super constructer

class super1:
    def __init__(self):
        print("parent constuter")

class super2(super1):
    def __init__(self):
        print("child constuter")
        super().__init__()
       # super1.__init__(self)

c=super2()#parent class   child constuter



