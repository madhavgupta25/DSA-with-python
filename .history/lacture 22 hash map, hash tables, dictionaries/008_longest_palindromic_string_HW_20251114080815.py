def longestPalindrome(s: str) -> int:
    freq_map = {}
    
    for ch in s:
        freq_map[ch] = freq_map.get(ch,0)+1
    length = 0
    odd_found = False
    
     
        

s = str(input())
print(longestPalindrome(s))
