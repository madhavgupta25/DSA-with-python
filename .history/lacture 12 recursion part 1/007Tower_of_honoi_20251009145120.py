def f (n:int,src:str,hlp:str,des:str)->None:
    #base case
    
    #recursive case
    f(n-1,src,dst,hlp)
    
    print()
    
n = map(int, input())
f(n, A , B , C)