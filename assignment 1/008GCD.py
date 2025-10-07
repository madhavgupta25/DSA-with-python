def GCD(a:int,b:int)->int:
    while b!=0:
        a,b=b,a%b
    return a
    
    
n1 = int(input("Enter the first number : ").strip())
n2 = int(input("Enter the value for second number : ").strip())
print("The GCD of the both numbers : ",GCD(n1,n2))