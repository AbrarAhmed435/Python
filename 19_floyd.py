

def floyd_warshall(adj):
    n = len(adj)

    D = [row[:] for row in adj]
    Pred = [[-1]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                D[i][j] = 0
            elif D[i][j] == 0:
                D[i][j] = float('inf')
            else:
                Pred[i][j] = i

    for x in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][x] + D[x][j] < D[i][j]:
                    D[i][j] = D[i][x] + D[x][j]
                    Pred[i][j] = Pred[x][j]

    return D, Pred
