cp=int(input("Enter cost price     : "))
sp=int(input("Enter selling  price : "))
p=sp-cp
print("Profit : ", p)
p+=(5/100)*p
print("New selling price : ", cp+p)