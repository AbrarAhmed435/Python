adj = [[1,2],[0,3],[0,3],[1,2]]
n = len(adj)
deg = [0] * n

def calculate_deg():
    for i in range(n):
        deg[i] = len(adj[i])

def dfs(u,path):
    while adj[u]:
        v=adj[u].pop()
        adj[v].remove(u)
        dfs(v,path)
    path.append(v)


def euler():
    calculate_deg()

    odd = []
    for i in range(n):
        if deg[i] % 2 == 1:
            odd.append(i)

    if len(odd) not in (0, 2):
        return None

    if len(odd) == 2:
        start = odd[0]   # Euler path
    else:
        start = next((i for i in range(n) if deg[i] > 0), 0)  # Euler circuit

    path=[]
    dfs(start,path)
    return path
