s = str(input().strip())
# print(s.swapcase()) #this is the one shortcut option or the standard option is :

result =""
for ch in s:
    if 'a' <=ch<= 'z':
        result+=chr(ord(ch)-32) # this is converting lower case to upper case
    elif 'A' <= ch <= 'Z':
        result += chr(ord(ch)+32) # this is converting uppercase to lowercase
    else:
        result+=ch
    
print(result)
        