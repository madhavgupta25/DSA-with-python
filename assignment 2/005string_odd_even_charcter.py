def string(s:str)->str:
    n = len(s)
    result = ""
    i = 0
    for ch in s:
        if i % 2 == 0:
            result+=chr(ord(ch)+1)
        else:
            result+=chr(ord(ch)-1)      
        i+=1
    return result
    
s = str(input().strip())
print(string(s))