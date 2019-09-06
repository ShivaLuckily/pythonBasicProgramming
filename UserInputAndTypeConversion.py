#Taking input from user and input function treat every input as string ,we need to typecast using input()


num1=input("enter the first number")#12
num2=input("enter the second number")#12
print(num1+num2) #1212


num1=input("enter the first number")#12
num2=input("enter the second number")#12
print(int(num1)+int(num2)) #24

num1=input("enter the first number")#12.4
num2=input("enter the second number")#12
print(float(num1)+int(num2)) #24.4


num1=input("enter the first number")#12.4
num2=input("enter the second number")#12
print(int(num1)+int(num2)) #error(decimal cannot convert to int)


num1=input("enter the first number")#12.4
num2=input("enter the second number")#12
print(float(num1)+float(num2)) #(float can store int number)