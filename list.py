

li=list([10,20,30])
print(li[1])
print(10 in li)
print(li[0:2])
print(sum(li))





li=list(["luck","boy","girl"])
print(li[1])
print(len(li))





list1=[11,13]
list2=[14,15]
list3=list1+list2
print(list3)
print(list2*3)




li=[3,2,4,5,6]
for i in li:
    print(i, end=" ")




lists=[x for x in range(10)]
print(lists)# 0 1 2 3 4 5 6 7 8 9

lists=[x+1 for x in range(10)]
print(lists)#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


lists=[x for x in range(10) if x%2==0]
print(lists)#[0, 2, 4, 6, 8]


list=[2,3,4,7]
print(list.remove(4))# remove the element from the list but doesnot return anything
print(list.pop(3))# remove the element from the list