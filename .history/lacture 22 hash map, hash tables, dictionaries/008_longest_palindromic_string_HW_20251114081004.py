def longestPalindrome(s: str) -> int:
    freq_map = {}
    
    for ch in s:
        freq_map[ch] = freq_map.get(ch,0)+1
    length = 0
    odd_found = False
    
    for val in freq_map.values():
        if val%2 == 0:
            length += val
        else:
            length+=val-1#when odd find
    
    if  
        

s = str(input())
print(longestPalindrome(s))
