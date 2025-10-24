def s(s:str)->list[s]:
    if not s:
        return 0
    

t = int(input("enter the number of test cases"))
for i in range (t):
    s = str(input().strip())
    
ans = f(s)