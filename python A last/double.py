class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        self.prev=None
    
class Double:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            
    #creation of double linked list
    def createDL(self,nodeValue):
        node=Node(nodeValue)
        node.prev=None
        node.next=None
        self.head=node
        self.tail=node
        return "The DLL is created successfully"
    
    def insertNode(self,nodeValue, location):
        if self.head is None:
            print('The node cannot be inserted')
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
                
            elif location==1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode
    
    #Traversal Method in Doubly Linked list
    def traverseDL(self):
        if self.head is None:
            print('There is no list')
        else:
            tempNode=self.head
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.next
                
    
    #reverse traversal
    def reverseDL(self):
        if self.head is None:
            print('No list')
        else:
            tempNode=self.tail
            while tempNode:
                print(tempNode.value)
                tempNode=tempNode.prev      
                
    #searching value and updating value
    def searchDL(self,old):
        if self.head is None:
            print('No list')
        else:
            tempNode=self.head
            while tempNode:
                if tempNode.value==old:
                    return tempNode.value
                tempNode=tempNode.next
            return 'The node doesnot exist'
    
    #deletion
    def deleteNode(self,location):
        if self.head is None:
            print('No list')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                tempNode=self.head
                index=0
                if index<location-1:
                    tempNode=tempNode.next
                    index+=1
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
            print('the node has been successfully deleted')

                
                    

                
                 
    
doubleLL=Double()
doubleLL.createDL(5)

print([node.value for node in doubleLL])
doubleLL.insertNode(0,0)
doubleLL.insertNode(2,1)
print([node.value for node in doubleLL])
#doubleLL.traverseDL()
#doubleLL.reverseDL()
print(doubleLL.searchDL(22))
doubleLL.deleteNode(0)
print([node.value for node in doubleLL])

        