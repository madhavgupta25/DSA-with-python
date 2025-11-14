def longestPalindrome(s: str) -> int:
    freq = {}
    
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    length = 0
    odd_found = False
    
    for c in freq.values():
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
