#1

a=20

if a>30:
    print("statement 1 ")
else:
    print("statement 2")



#2
a=20
if True:
    print("statement 1 ")
else:
    print("statement 2")

#3

a=31
if a%2==0:
    print("even")
else:
    print("odd")

#4
a=31
if a%2==0:
    print("even")
else:
    print("odd")

print("not a part of if & else")

#5 single line

print("first statement") if 20>10 else print("second statement")

print("first statement"),print("second statement")if 20>10 else print("third statement")


#6 elif condition

a=30
if a>40:
    print("a")
elif a==30:
    print("b")

elif a < 10:
    print("c")
