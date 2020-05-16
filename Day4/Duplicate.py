E={}
A={}
n=int(input("Enter the number of key value pairs : "))
for x in range(n):
    key=input("Enter the key:")
    value=input("Enter the value :")
    E[key]=value
    print("The dictionary is :")
print(E)
for key,value in E.items():
    if value not in A.values():
        A[key]=value
print("the dictionary after removal of duplicate values is :",A)