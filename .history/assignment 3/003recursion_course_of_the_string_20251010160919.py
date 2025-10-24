def get_codes(s:str)->list[str]:
    # base case:empty string
    if len(s) == 0:
        return ""
    
    #base case:single digit
    if len(s) == 1:
        if s(0) == '0':
            return []
        return [chr(int(s[0])+96)] #+96 means 1+96 = a in python lang
    
    result = []
    
    # recursive case:
    # take one digit:
    if len(s) == 1:
        

s = str(input())
ans = get_codes(s)
print(ans)