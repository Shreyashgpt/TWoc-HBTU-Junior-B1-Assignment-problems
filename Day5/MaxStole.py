def vstolen(list1,n):
    t=0
    if n==0:
        print("value stolen is :",n)
    elif n==1:
        print("Value stolen is :",list1[n])
    else:
        for x in range(0,n,2):
            t=t+list1[x]
    print("Value stolen is :",t)
    

list2=[]
l=int(input("Enter the size of the list :"))
for x in range(l):
    e=int(input("Enter the item : "))
    list2.append(e)
vstolen(list2,l)