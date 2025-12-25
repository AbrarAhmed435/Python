n=len(adj)

status=[0]*n
predecessor=[None]*n


pathlength=[float('inf')]*n

def min_node(adj):
    k=-1
    min=float('inf')
    for i in range(len(adj)):
        if status[i]==0 and pathlength[i]<min:
            k=i
            min=pathlength[i]
    return k

def djistra(adj):
    pathlength[0]=0
    predecessor[0]=0

    while True:
        current=min_node(adj)
        if current==-1:
            return 
        status[current]=1

        for i in range(n):
            if adj[current][i] and  not status[i]:
                if pathlength[i]>(pathlength[current]+adj[current][i]):
                    pathlength[i]=pathlength[current]+adj[current][i]
                    predecessor[i]=current




def path(source,destination):
    k=destination
    path=[destination]
    while k!=source:
        k=predecessor[k]
        path.append(k)
    path.reverse()
    cost=pathlength[destination]-pathlength[source]





