def is_palindrome(ss:str)->bool:
    return ss == ss[::-1]


def longest_substring(s:str)->int:
    res = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if is_palindrome(s[i:j]):
                length = len(s[i:j])
                res = max(res,length)
    return max
    
s = str(input())
print(longest_substring(s))