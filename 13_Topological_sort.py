
def topo(adj):
    n=len(adj)
    indegree=[0]*n
    for i in range(n):
        for j in adj[j]:
            indegree[i]+=1
    
    queue=[]

    for i in range(0,len(indegree)):
        if indegree[i]==0:
            queue+=[i]

    order=[]

    while len(queue)!=0:
        x=queue[0]
        queue=queue[1:]
        order+=[x]

        for j in adj[x]:
            indegree[j]-=1
            if indegree[j]==0:
                queue+=[j]
    
    return order
        


        