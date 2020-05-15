n1 = int(input("Enter number of elements in list1 : "))
print("Enter elements of list1 : ")
list1=[]
for x in range(n1):
    list1.append(input())
n2 = int(input("Enter number of elements in list2 : "))
print("Enter elements of list2")
list2 = []
inter =[]
for x in range(n2):
    list2.append(input())
    if list2[x] in list1:
        if list2[x] in inter:
            pass
        else:
            inter.append(list2[x])
print("Intersection : ", inter)
        