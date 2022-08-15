def prepend(self,data):
    new_node=Node(data)
    if self.head==None:
        self.head=new_node
    else:
        new_node.next=self.head
        self.head=new_node
        
        
