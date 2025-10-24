def f(n:int) -> int:
    #base case
    if n==1:
        return 0
    #recursive case
    
    #f(n = finds the minimum steps to reach 1)
    
    # decide the next option
    
    # option 1: n-1
    op1 = f(n-1)
    
    # option 2 : reduce n to n/2 assuming n%2 is zero
    op2 = sys.maxsize
    if n%2 == 2:
        op2 = f(n/2)
        
    # option 3 : reduce n to n/3 assuming n%3 is zero
    op3 = sys.maxsize
    if n%3 == 0:
        op3 = f(n/2)
        
    return 1+min(op1, op2, op3)
n = int(input())
print(f(n))