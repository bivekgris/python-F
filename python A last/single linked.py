from cmath import sin


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Slinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        
singlelinked=Slinkedlist()
node1=Node(1)
node2=Node(2)

singlelinked.head=node1
singlelinked.head.next=node2
singlelinked.tail=node2
        