def get_codes(s:str)->str:
    # base case:empty string
    if len(s) == 0:
        return [""]
    
    #base case:single digit
    if len(s) == 1:
        if s[0] == '0':
            return []
        return [chr(int(s[0])+96)] #+96 means 1+96 = a in python lang
    
    result = []
    
    # recursive case:
    # take one digit:
    if s[0]!='0':
        first_char = chr(int(s[0])+96)
        for code in get_codes(s[1:]):
            result.append(first_char + code)
    
    # take two digit:
    two_digit = int(s[:2])
    if 10 <= two_digit <= 26:
        second_char = chr(two_digit+96)
        for code in get_codes(s[2:]):
            result.append(second_char+code)
            
    return result
    
        
        
        

s = str(input().strip())
ans = get_codes(s)

print("[" + ",")

# this is also code which i write in assignment
# def allc(s):
#     if not s: return [""]
#     r=[]
#     if s[0]!="0":
#         for p in allc(s[1:]):
#             r.append(chr(96+int(s[0]))+p)
#     if len(s)>1 and 10<=int(s[:2])<=26:
#         for p in allc(s[2:]):
#             r.append(chr(96+int(s[:2]))+p)
#     return r

# x=input().strip()
# print("[" + ", ".join(allc(x)) + "]")
