E=dict()
l=""
s=""
n=int(input("Enter the number of key : value pairs : "))
for x in range(n):
    print("Enter the key for dictionary:")
    ekey=input()
    print("Enter the value for the dictionary:")
    evalue=input()
    E[ekey]=evalue
print(E)
print("The second largest value in the dictionary is:")
for x in E:
    for y in E:
        if (E[x]>E[y] and x!=y):
            l=E[x]
for x in E:
    for y in E:
        if (E[x]>E[y] and E[x]<l):
            s=E[y]
print(s)