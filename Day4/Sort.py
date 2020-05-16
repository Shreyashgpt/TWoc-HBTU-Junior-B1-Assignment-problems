list1=[]
n=int(input("Enter the size of tuple:"))
for i in range(n):
    e=input("Enter the element:")
    list1.append(e)
list1.sort()
tuple1=tuple(list1)
print(tuple1)