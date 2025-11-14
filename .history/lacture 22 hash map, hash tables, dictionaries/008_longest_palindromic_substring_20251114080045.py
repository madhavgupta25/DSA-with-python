def is_palindrome(ss:str)->bool:
    return ss == ss[::-1]


def longest_substring(s:str)->int:
    res = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                res = max(res,length)
    return res
    
s = str(input())
print(longest_substring(s))