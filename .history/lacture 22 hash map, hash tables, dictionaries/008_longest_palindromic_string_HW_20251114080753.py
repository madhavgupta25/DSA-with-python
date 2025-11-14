def longestPalindrome(s: str) -> int:
    freq_map = {}
    
    for ch in s:
        freq_map[ch] = freq_map.get(ch,0)+1
    length = 0
     
        

s = str(input())
print(longestPalindrome(s))
