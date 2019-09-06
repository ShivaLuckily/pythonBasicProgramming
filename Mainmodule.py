#Approach 1

import moduleOperation

str=moduleOperation.add(10,20)
str1=moduleOperation.mul(30,40)
print(str)
print(str1)

#Approach 2

from moduleOperation  import  *

add(10,20)
mul(30,40)
print(add(10,20))
print(mul(30,40))


########ANOTHER EXAMPLE FROM MODULE OPERATION CLASS

from moduleOperation import *

obj = Animal()
obj.fly()