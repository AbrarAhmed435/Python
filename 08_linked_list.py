class Node:
    def __init__(self,data):
        self.data=data
        self.next=None



class LinkedList:
    def __init__(self):
        self.head=None


    def append(self,data):
        new_Node=Node(data)

        if self.head is None:
            self.head=new_Node
            return 
        
        temp=self.head
        while temp.next is not None:
            temp=temp.next

        temp.next=new_Node
    
    def prepend(self,data):
        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return 
        
        new_Node.next=self.head
        self.head=new_Node

    def insert_at_index(self,data,index):
        if index<1:
            print("Invalid index")
            return 
    

        new_Node=Node(data)

        if index==1:
            self.prepend(data)
            return 

        temp=self.head

        while index>2:
            if temp is None:
                print("Index Out of bounds")
                return 
            temp=temp.next
            index=index-1
        
        if temp is None:
            print(f"Less than {index} nodes present in Linked List")

        if temp.next is None:
            temp.next=new_Node
            return

        new_Node.next=temp.next

        temp.next=new_Node


    def print_list(self):
        temp=self.head
        while temp:
            print(temp.data, end="->")
            temp=temp.next

        print("None")


l=LinkedList()

l.insert_at_index(8,5)


l.prepend(8)
l.append(10)
l.prepend(9)



l.print_list()
l.insert_at_index(21,7)
l.print_list()