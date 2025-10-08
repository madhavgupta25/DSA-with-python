s = str(input().strip())

result = ""

for i in range(1,len(s)):
    result+=s[i-1]
    a = ord(s[i])- ord(s[i-1])
    result+=str(a)
    
    
result+=s[-1]
print(result)