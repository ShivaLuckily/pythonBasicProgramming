'''class overiding:
    i=10
    def display(self):
        print("parent class")

class over(overiding):
    i=20
    def display(self):
        print("child class")

c=over()
c.display()
print(c.i)'''

######## overloading  #########


class overloading:

    def display(self,a=None,b=None):

        if a!=None and  b!=None:
         print(" a & b")
        elif a!=None:
            print("a")
        else:
            print("empty")



c=overloading()
c.display(10,20) # a & b
