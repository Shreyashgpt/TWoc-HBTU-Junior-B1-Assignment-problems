d=[]
c=0
s=""
n=int(input("Enter the size:"))
for x in range(n):
    e=input("Enter")
    d.append(e)
print(d)
t=tuple(d)
for x in t:
    if t.count(x)>c:
        c=t.count(x)
for x in t:
    for y in t:
        if (t.count(x)==c and t.count(y)==c and x!=y):
            if x<y:
                s=x
            elif x>y:
                s=y
print("The winner is:",s)