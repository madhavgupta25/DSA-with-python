def subsequence(s:str)->list[str]:
    # base case:
    if not s:
        return [""]
    
    # recursive case:
    r = subsequence[1:]


s = str(input().strip())
ans = subsequence(s)
