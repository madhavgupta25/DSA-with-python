def longest_substring(s:str)->int:
    for i in range(len(s)):
        for j in range(len(s)):
            if is_palindrome(s[i:j]):
                
    
s = str(input())
print(longest_substring(s))