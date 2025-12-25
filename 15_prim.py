def prim(adj):
    list=[]
    n=len(adj)
    visited=[False]*n
    visited[0]=True

    for count in range(n-1):
        val=float('inf')
        u=-1
        v=-1

        for i in range(n):
            if visited[i]:
                for j in range(n):
                    if adj[i][j] and not visited[j]:
                        if adj[i][j]<val:
                            val=adj[i][j]
                            u=i
                            v=j

        if v!=-1:
            visited[v]=True
            list+=[[u,v]] 