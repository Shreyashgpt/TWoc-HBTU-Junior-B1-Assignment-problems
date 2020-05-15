S = input("Enter a string : ")
l = len(S)
new = ""
for x in range(l):
    if S[x] not in S[x+1 : ]:
        new = new + S[x]
print("String after removing duplicate characters is : ", new)