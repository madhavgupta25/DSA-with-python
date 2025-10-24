def path(r:int,c:int,s:str)->str:
    # base case
    if r == 1 and c ==1:
        return [s]
    # recursive case
    out = []
    if r>1:
        out+=path(r-1,c,s+"V")
    if c>1:
        out+=path(r,c-1,s+"H")
    if r>1 and c>1 and r == 2 :
        out+=path(r-1,c-1,s+"D")
    return out
        

n1 = int(input().strip()) # number of rows
n2 = int(input().strip()) # number of columns
ans = path(n1,n2,"")
print(" ".join(ans))
print(len(ans))