'''from abc import  ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        pass

class B(A):
    def display(self):
        print("complete")

c=B()
c.display()'''

################

from abc import  ABC ,abstractmethod

class A(ABC):
    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def display1(self):
        pass

class B(A):
    def display(self):
        print("complete")

class C(B):
    def display1(self):
        print("complete under C")


c=C()
c.display1()


###################### constructer in abstract class

from abc import  ABC ,abstractmethod

class A(ABC):

    def __init__(self,value):
      self.value=value


    @abstractmethod
    def display(self):
        pass

class B(A):
    def display(self):
        print(self.value + 100)

c=B(100)
c.display()

