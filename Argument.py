from _ast import keyword


def sum(*args):
    s=0
    for i in args:
        s=s+i
        print(s)

sum(1,2,3)#1,3,6


#################single argument

def mulArg(a,b,c):
    print(a,b,c)

args=[2,4,6]

mulArg(*args)


#################        Multiple argument


def mul(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

mul(name='lucky',rollno='200')





