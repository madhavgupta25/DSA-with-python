def get_codes(s:str)->list[str]:
    # base case:empty string
    if len(s) == 0:
        return ""
    
    #base case:single digit
    if len(s) == 1:
        if s(0) == '0':
            return []
        return [chr(int(s[0])+96)] #

s = str(input())
ans = get_codes(s)
print(ans)