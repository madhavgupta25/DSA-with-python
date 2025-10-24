def f(s:str,i:int)->list[s]:
    # base case
    if i == len(s):
        return ["".join(s)]
    
    # recursive case
    result = []
    if s[i] == '?':
        s[i] = '0' # replace ? with 0
        result += f(s,i+1) # after replacing we call s for i+1
        
        s[i] = '1' # replace ? with 1
        result += f(s,i+1) # after replacing we call s for i+1
        
        #backtrack
        s[i] = '?' # this is for 
        

t = int(input("enter the number of test cases"))
for i in range (t):
    s = str(input().strip())
    
ans = f(s,0)