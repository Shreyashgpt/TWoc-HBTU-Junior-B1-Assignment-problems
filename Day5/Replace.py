def Replace(n):
    x=0
    s=0
    while n!=0:
        d=n%10
        if d==0:
            d=5
            s=s+d*10**x
        else:
            s=s+d*10**x
        n=n//10
        x+=1
    print("New integer is:",s)

num =int(input("Enter an integer :"))
Replace(num)