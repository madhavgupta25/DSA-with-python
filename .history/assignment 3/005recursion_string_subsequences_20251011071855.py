def subsequence(s:str):
    # base case:
    if not s:
        return [""]
    
    # recursive case:
    r = subsequence(s[1:]
    x = s[0]
    a = str(ord(x))
    result = r+[x+p for p in r]+[a+p for p in r]
    
    return result


s = str(input().strip())
ans = subsequence(s)
print(" ".join(ans))
print(len(ans))
