def fact(n:int)->int:
    #base case
    if n == 0:
        return 1
    
    
    #recursive case
    a = fact(n-1)
    return n*a
    
n = int(input("Enter the number : "))
print("The Factorial of ",n," is ",fact(n))
