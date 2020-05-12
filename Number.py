n=int(input("Enter a number : "))
c=0
arm=0
rev=0
if n%2==0:
    print("Number is Even")
else:
    print("Number is Odd")
for x in range(1,n):
    if n%x==0:
        c+=1
        if c>1:
            break
if c>1:
    print("Number is Not Prime")
else:
    print("Number is Prime")
copy=n
while n>0:
    d=n%10
    arm+=(d*d*d)
    rev=rev*10
    rev+=d
    n=n//10

if rev==copy:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
if arm==copy:
    print("Number is Armstong")
else:
    print("Number is Not Armstrong")