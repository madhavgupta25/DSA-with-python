def path(r:int,c:int,s:str)->str:
    # base case
    if r == 1 and c ==1:
        return s
    # 
    out = []
    if c>1:
        out+=path(r,c-1,s+"V")
    if r>1:
        out+=path(r-1,c,s+"H")
    if c>1 and r>1:
        out+=path(r-1,c-1,s+"D")
    
    return out
        

n1 = int(input().strip()) # number of rows
n2 = int(input().strip()) # number of columns
ans = path(n1,n2,"")