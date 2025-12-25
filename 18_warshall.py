


def warshal(adj):
    n=len(adj)

    P=adj

    for x in range(n):
        for i in range(n):
            for j in range(n):
                if not P[i][j]:
                    if P[i][x] and P[x][j]:
                        P[i][j]=1


