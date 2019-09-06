###Single inherientance

'''class parent:
    a,b=10,20
    def diplay(self):
        print(self.a,self.b)

class child(parent):
    c,d=30,40
    def diplay1(self):
        print(self.c,self.d)

c=child()
c.diplay()
c.diplay1()'''

##Single Inherence
'''
class parent:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def diplay1(self):
        print(self.a,self.b)

class child(parent):

    def __init__(self, c, d):
        self.c = c
        self.d = d

    def diplay(self):
        print(self.c, self.d)

c=child(30,40)
c.diplay()

c1=parent(50,60)
c1.diplay1()
'''

########   Multiple inheritence ############

class A:
    def __init__(self):
        self.str="lucky"
        print("parent class A")

class B:
    def __init__(self):
        self.str1="Mohanty"
        print("parent class B")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("child c")

    def display(self):
        print(self.str)
        print(self.str1)

c1=C()
c1.display()
