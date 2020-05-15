l = int(input("Enter number of elements in list : "))
List = []
print ("Enter elements of list : ")
for x in range (l):
    List.append(input())
newList = [List[0]]
for x in range (l):
    if List[x] not in List[0:x-1]:
        newList.append(List[x])
print ("New list : ", newList)