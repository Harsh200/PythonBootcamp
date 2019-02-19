list1 = [1,2,3,4]
print( list1[0])
list2=["harsh",[1,2,3],"vishi"]
print(list2[0],[0])
list2[2]=123
print(list2)
list1[0]=2
list1[1:4]=[1,2,3,4]
print(list1)
del(list1[1])
list1.remove(4)
print("After deletion ",list1)