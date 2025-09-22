def f (inp:list[int], i:int, counter:list[int], k:int)->None:

    if i == n:
        counter[0] += 1
        if counter[0] == k:   # print only kth permutation
            print("".join(inp))
        return
    
    for j in range(i, len(inp)):
        inp[i], inp[j] = inp[j], inp[i]
        f(inp, i+1, counter, k)
        inp[i] , inp[j] = inp[j], inp[i] # backtracking




n = 3
k = 3
inp = []

for i in range(1, n+1):
    inp.append(str(i))   # store as string

# # print(inp)              # prints ['1', '2', '3']
s = "".join(inp)        # join list into a string
# print(s)                # prints 123
counter = [0] 
f(inp, 0, counter, k)