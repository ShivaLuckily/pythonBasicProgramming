#####Wite to file

f=open('D:\\python.txt', 'w')
f.write('write to python file\n')
f.write('write to python file2\n')
f.close()


########Read to file


f=open("D:\\python.txt", "r")
print(f.read())
#write to python file
#write to python file2

print(f.read(10))#write to p
f.close()



######for loop

f=open("D:\\python.txt", "r")
for i in f:
 print(i)
f.close()