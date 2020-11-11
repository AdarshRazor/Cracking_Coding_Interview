import os
os.system('cls')

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def appendnode(self,data):
        New_Node = Node(data)
        if self.head==None:
            self.head=New_Node
            return
        
        last_node=self.head
        while last_node.next!=None:
            last_node=last_node.next
        last_node.next=New_Node
    
    def printnode(self):
        Curr_Node=self.head
        while Curr_Node!=None:
            print("(",Curr_Node.data,end=" ) --> ")
            Curr_Node=Curr_Node.next
        print("\n")
        
    def conv(self):
        curr_node=self.head
        string=""
        while curr_node is not None:
            string+=str(curr_node.data)
            curr_node=curr_node.next
        return(string)

#test case 1:

ll1=LinkedList()

ll1.appendnode(1)
ll1.appendnode(2)
ll1.appendnode(3)
ll1.appendnode(6)
ll1.appendnode(7)
ll1.appendnode(4)
ll1.printnode()

palin=ll1.conv()
if palin==palin[::-1]:
    print("Linked list is palindrome\n")
else:
    print("Linked list is not a palindrome\n")
#test case 2:

ll=LinkedList()

ll.appendnode(1)
ll.appendnode(2)
ll.appendnode(3)
ll.appendnode(3)
ll.appendnode(2)
ll.appendnode(1)
ll.printnode()

palin=ll.conv()
if palin==palin[::-1]:
    print("Linked list is palindrome\n")
else:
    print("Linked list is not a palindrome\n")