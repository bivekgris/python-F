def append(self,data):
    new_node=Node(data) #create the new node
    
    if self.head==None:
        self.head=new_node
    else:
        curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
        

    