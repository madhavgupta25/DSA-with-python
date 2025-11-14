def longestPalindrome(s: str) -> int:
    freq_map = {}
    
    for ch in s:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    
    length = 0
    odd_found = False
    
    for c in freq_map.values():
        if c % 2 == 0:
            length += c
        else:
            length += c - 1
            odd_found = True
    
    # If any odd count exists, add 1 for center character
    if odd_found:
        length += 1
    
    return length

s = str(input())
print(longestPalindrome(s))
