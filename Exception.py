'''print("start")

try:
  print(10/0)
except NameError:
    print("name exception handled")
except:
    print("exception handled")
else:
    print("entered else body")
finally:
    print("finally block")'''

#########################

def enterage(age):
    if age < 0:
        raise ValueError("value error handle")

    if age%2==0:
        print("even age")
    else:
        print("age odd")

try:
  enterage(-1)
except:
    print("value error in except block")
