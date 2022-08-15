class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        
    def print_list(self):
        cur_node=self.head
        while cur_node!=None:
            print(cur_node.data)
            cur_node=cur_node.next
            
llist=LinkedList()

llist.head=Node(1)
second=Node(2)
third=Node(3)

llist.head.next=second
second.next=third

llist.print_list()