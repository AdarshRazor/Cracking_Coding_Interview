'''
code to remove duplicates from an unsorted linked list.
'''

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

    def checkdups(self):
        dups=[]
        node=self.head
        while node is not None:
            if node.data not in dups:
                dups.append(node.data)
                prev=node
                node=node.next                
            else:
                prev.next=node.next
                node=node.next

ll=LinkedList()

ll.appendnode(6)
ll.appendnode(3)
ll.appendnode(8)
ll.appendnode(1)
ll.appendnode(3)
ll.appendnode(2)
ll.appendnode(7)
ll.appendnode(1)
ll.printnode()
print("Removing Dups . . .\n")
ll.checkdups()
ll.printnode()