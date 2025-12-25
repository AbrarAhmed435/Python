n=len(adj)

status=[0]*n
predecessor=[None]*n


pathlength=[float('inf')]*n

def bell(edges):
    pathlength[0]=0
    predecessor[0]=0

    for i in range(n): ## it should n-1 ,nut we want to detect cycle
        for e in edges:
            u=e[0]
            v=e[1]
            weight=e[2]
            if pathlength[u]!=float('inf') and pathlength[v]>pathlength[u]+weight:
                if i==n-1:
                    print("Negative cycle loop detected")
                    return 
                pathlength[v]=pathlength[u]+weight
                predecessor[v]=u
                


#####################
# Negative cycle problem

# After v-1 loops we do it again if if pathlength[v]!=float('inf') pathlength[v]>pathlength[u]+weight: again satisfy there is negative loops because after v-1 iteration grpah should be stable
