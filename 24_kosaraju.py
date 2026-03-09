def dfs1(visited, index, adj, n, st):
    visited[index] = True
    for i in range(n):
        if adj[index][i] and not visited[i]:
            dfs1(visited, i, adj, n, st)
    st.append(index)

def dfs2(visited, index, adj, n, component):
    visited[index] = True
    component.append(index)
    for i in range(n):
        if adj[index][i] and not visited[i]:
            dfs2(visited, i, adj, n, component)

def kosaraju(adj):
    n = len(adj)
    visited = [False] * n
    st = []

    # Step 1: DFS and fill stack
    for i in range(n):
        if not visited[i]:
            dfs1(visited, i, adj, n, st)

    # Step 2: Transpose graph
    transpose = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if adj[i][j]:
                transpose[j][i] = 1

    # Step 3: DFS on transposed graph
    visited = [False] * n
    components = []

    while st:
        index = st.pop()
        if not visited[index]:
            component = []
            dfs2(visited, index, transpose, n, component)
            components.append(component)

    return components
