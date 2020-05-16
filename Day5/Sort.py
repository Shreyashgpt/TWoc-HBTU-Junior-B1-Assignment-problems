def sorter(list1):
    e=[]
    o=[]
    for x in list1:
        if x%2==0:
            e.append(x)
        else:
            o.append(x)
    e.sort()
    o.sort(reverse=True)
    print(e)
    print(o)
    
    
list2=[]
n=int(input("Enter the size of list :"))
for x in range(n):
    e=int(input("Enter the list member :"))
    list2.append(e)
print(list2)
sorter(list2)