from collections import deque

n , m = map(int, input().split())
adj = [[] for _ in range(n)]
for _ in range(m):
    u ,v = map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
    
s = 0 

vis = [False]*n
q = deque()

vis[s] = True
q.append(s)

dis = [None] * n
dis[s] = 0

while q:
    cur = q.popleft()
    for ngb in adj[cur]:
        if not vis[ngb]:
            vis[ngb] = True
            q.append(ngb)
            dis[ngb] = dis [cur]+1
            
for i in range (n):
    print(f"dis({i}) = dis[{i}]")
            