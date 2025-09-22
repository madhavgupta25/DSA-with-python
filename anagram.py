def isAnagram(s: str, t: str) -> bool:
    u = ""
    for ch in s:
        u = ch + u 
    
    return u == t


s = "anagram"
t = "margana"
print(isAnagram(s, t))  # True
