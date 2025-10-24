def f(s:str, out:list[str], i:int)->None:
    
    # base case
    if i == len(s):
        print("".join(out))
        return
    # recursive case

    # f(i) = take decision for s[i.....n-1]

    # decide for s[i]

    # option 1: include s[i] to out[]
    out.append(s[i])
    f(s, out, i+1)
    out.pop() # backtracking step which is more important for this question 
              # backtrack means delete what we output generate and clear from memory

    # option 2: exclude s[i] from out[]
    f(s, out, i+1)


# time complexity : O(2^n)
# space complexity : O(n)
s="abc"
out=[]
f(s, out , 0)