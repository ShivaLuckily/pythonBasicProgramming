
a,b=10,20#global variable

class varibale:
    a,b=30,40#class variable

    def display(self,a,b):

        print(a+b)#access the local varibale
        print(self.a+self.b)# access the class varibale
        print(globals()['a']+globals()['b'])

mc=varibale()
mc.display(200,222)#422 70 30


