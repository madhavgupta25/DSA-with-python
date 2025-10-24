def path(r:int,c:int,s:str)->str:
    # base case
    if r == 1 and c ==1:
        return s
    out = []
    if r>

n1 = int(input().strip()) # number of rows
n2 = int(input().strip()) # number of columns
ans = path(n1,n2,"")