def f(s:str)->str:
    
    result = ""
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count+=1
        else:
            result +=s[i-1]
            
            if count > 1:
                result+=str(count)
                count = 1
        
    result+=s[-1]
    if count>1:
        result+=str(count)
    
    return result
            


s = str(input("Enter the string : ").strip())
print(f(s))