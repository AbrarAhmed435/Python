class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class BinaryTee:
    def __init__(self):
        self.root=None

    def insert(self,data):
        new_Node=Node(data)

        if self.root is None:
            self.root=new_Node
            return 
        
        parent=None
        curr=self.root

        while curr is not None:
            parent=curr
            if data<curr.data:
                curr=curr.left
            elif data>curr.data:
                curr=curr.right
            else:
                print("Ambigous node")
                return 
            if data<parent.data:
                parent.left=new_Node
            else:
                parent.right=new_Node
                
    

    def inorder(self,node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data,end=" ")
        self.inorder(node.right)
        
