def dfs(adj,index,visited,traversal):
    traversal+=[index]
    visited[index]=True
    for i in range(0,len(adj)):
        if adj[index][i] and not visited[i]:
            dfs(adj,i,visited,traversal)


def Transpose(adj):
    for i in range(0,len(adj)):
        for j in range(0,i):
            temp=adj[i][j]
            adj[i][j]=adj[j][i]
            adj[j][i]=temp
    

def is_Strongly_Connected(adj,visited):
    before=[]
    after=[]

    dfs(adj,0,visited,before)
    if len(before)<len(adj):
        return False
    Transpose(adj)

    visited=[False]*len(adj)

    dfs(adj,0,visited,after)

    if len(after)<len(adj):
        return False
    return True





