def is_palindrome(:str)->bool:
    return s == s[::-1]
def longest_substring(s:str)->int:
    for i in range(len(s)):
        for j in range(len(s)):
            if is_palindrome(s[i:j]):
                
    
s = str(input())
print(longest_substring(s))