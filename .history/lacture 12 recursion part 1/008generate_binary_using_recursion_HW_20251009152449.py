def f(n:int)->None:
    #base case
    if n == 0:
        return ""
    
    return f()
    # recursive call
    def helper(n:int)->int:
        if n == 0:
            return ""
        
        return helper(n//2) + str(n%2)
    
    return helper(n)
        

n = int(input())
print(f(n))