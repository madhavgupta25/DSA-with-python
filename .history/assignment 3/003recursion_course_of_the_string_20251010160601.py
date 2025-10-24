def get_codes(s:str)->list[str]:
    # base case:empty string
    if len(s) == 0:
        return ""
    
    #base case

s = str(input())
ans = get_codes(s)
print(ans)