from collections import deque

def bfs(adj,start):
    n=len(adj)
    visited=[False]*n
    waiting=[False]*n

    dq=deque()

    dq.append(start)
    waiting[start]=True

    while len(dq):
        x=dq.popleft()
        print(x)
        visited[x]=True
        for i in range(n):
            if adj[x][i] and not visited[i] and not waiting[i]:
                dq.append(i)
                waiting[i]=True



