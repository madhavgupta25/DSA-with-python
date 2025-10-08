def is_palindrome(s:str)->bool:
        return s == s[::-1]
    

s = str(input().strip())
n = len(s)
count = 0
for i in range(n):
    for j in range(i+1,n+1):
        if is_palindrome(s[i:j]):
            count+=1
            
print(count)
        


