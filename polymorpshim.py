'''class poly:
    __i=10

    def display(self):
       print(self.__i)


c=poly()
print(c._poly__i)# we cannot acces directly like c.__i in python but in java we can




#########
class poly:
    __i=10

    def display(self):
       print(self.__i)
class poly1(poly):
    j=20
    def display1(self):
       print(self.__i)

o=poly1()
print(o.__i)# cannot call private data'''


###Private variable

class poly:
    __i=10

    def display1(self,a):
        self.__i=a

    def display(self):
       print(self.__i)

o=poly()

o.display1(50)# updating the private variable indirectly

o.display()
