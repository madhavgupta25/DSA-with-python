def subsequence(s:str)->list[str]:
    # base case:
    if not s:
        return [""]
    
    # recursive case:
    r = subsequence[1:]
    x = s[0]
    a = str(ord(x))
    result = r+[x+p for p in r]+[a+p for p in x]
    return 


s = str(input().strip())
ans = subsequence(s)
