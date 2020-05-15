S=input("Enter a string : ")
l=len(S)
rev = ""
for x in range(l):
    rev += S[l-1]
    l -= 1
print ("Reverse of string is : ", rev)