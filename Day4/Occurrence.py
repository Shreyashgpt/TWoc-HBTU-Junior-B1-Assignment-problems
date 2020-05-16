LIST=[]
n=int(input("Enter the size :"))
for i in range(n):
    E=input("Enter the element :")
    LIST.append(E)
TUPLE=tuple(LIST)
print(TUPLE)
a=input("Enter the element whose occurence is to be printed :")
print(TUPLE.count(a))