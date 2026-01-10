class BTreeNode:
    def __init__(self,leaf=True):
        self.keys=[]
        self.children=[]
        self.leaf=leaf


class BTree:
    def __init__(self,m=4):
        self.root=BTreeNode()
        self.m=m
        self.max_keys=m-1

    def split_child(self,parent,i):
        m=self.m
        full_child=parent.children[i]
        mid=self.max_keys//2

        print(f"Splitting node {full_child.keys}")

        new_node=BTreeNode(leaf=full_child.leaf)

        parent.keys.insert(i,full_child.keys[mid])
        new_node.keys=full_child.keys[mid+1:]
        full_child.keys=full_child.keys[:mid]

        if not full_child.leaf:
            new_node.children=full_child.children[mid+1:]
            full_child.children=full_child.children[:mid+1]

        parent.children.insert(i+1,new_node)

    def insert_non_full(self,node,key):
        i=len(node.keys)-1

        if node.leaf:
            node.keys.append(None)
            while i>=0 and key<node.keys[i]:
                node.keys[i+1]=node.keys[i]
                i-=1
            node.keys[i+1]=key
            print(f"Inserted {key} into left {node.keys}")
        else:
            while i>=0 and key<node.keys[i]:
                i-=1
            i+=1

            if len(node.children[i].keys)==self.max_keys:
                self.split_child(node,i)
                if key>node.keys[i]:
                    i+=1
            self.insert_non_full(node.children[i],key)

    def insert(self,key):
        root=self.root
        if len(root.keys)==self.max_keys:
            print("Root full ->splitting root")
            new_root=BTreeNode(leaf=False)
            new_root.children.append(root)
            self.split_child(new_root,0)
            self.root=new_root
            self.insert_non_full(root,key)
        else:
            self.insert_non_full(root,key)
    
    def inorder(self,node):
        if node is None:
            return 
        n=len(node.keys)

        for i in range(n):
            if not node.leaf:
                self.inorder(node.children[i])
            
            print(node.keys[i],end=" ")
        
        if not node.leaf:
            self.inorder(node.children[n])

bt = BTree(m=4)

keys = [10, 20, 5, 6] # 12, 30, 7, 17]

for k in keys:
    print(f" Inserting {k}")
    bt.insert(k)

print(bt.root.keys)
