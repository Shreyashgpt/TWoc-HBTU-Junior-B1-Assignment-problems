def shift(list1,n):
    t=0
    for x in range(n):
        for y in range(x+1,n):
            if list1[x]<list1[y]:
               t=list1[x]
               list1[x]=list1[y]
    print(list1)          
            
n=int(input("Enter the size of the list :"))
list2=[]
for x in range(n):
    e=int(input("Enter member %d :"%(x+1)))
    list2.append(e)
print(list2)
shift(list2,n)