def f(s:str,i:int)->list[s]:
    # base case
    if i == len(s):
        return ["".join(s)]
    
    # recursive case
    result = []
    if s[i] == '?':
        s[i] = '0'
        result += f(s)

t = int(input("enter the number of test cases"))
for i in range (t):
    s = str(input().strip())
    
ans = f(s)