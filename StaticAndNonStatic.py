class Test:
    def display(self):
     print("non static")

    @staticmethod
    def display1():
      print("static")

t=Test()
t.display()
Test.display1()