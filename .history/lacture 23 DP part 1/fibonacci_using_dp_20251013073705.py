cnt1 = 0
cnt2 = 0
def f(n:int)->int:
    global cnt1
    cnt1+=1
    # base case
    if n == 0 or n == 1:
        return n
    
    #recursive case
    a = f(n-1)
    b = f(n-2)
    return a+b

def f_topdown(n:int,dp:list[int])->int:
    global cnt2
    cnt+=2
    # lookup
    if dp[n]!= -1:
        return dp[n]
    # base case
    if n == 0 or n == 1:
        dp[n] = n
        return dp[n]
    
    #recursive case
    a = f_topdown(n-1,dp)
    b = f_topdown(n-2,dp)
    dp[n] = a+b
    return dp[n]

n = int(input().strip())
print(f(n))

dp = [-1]*(n+1)
print(f_topdown(n,dp))
print(cnt1)
print(cnt1)
