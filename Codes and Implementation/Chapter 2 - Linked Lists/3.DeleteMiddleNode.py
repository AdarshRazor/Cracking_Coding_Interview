'''
delete the middle node
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

    def deleteat(self,pos):
        if pos==1:
            self.head=self.head.next
            return
        Curr_Node=self.head
        for pos in range(0,pos-1):
            Prev_Node=Curr_Node
            Curr_Node=Curr_Node.next
        Prev_Node.next=Curr_Node.next

ll=LinkedList()

ll.appendnode(1)
ll.appendnode(2)
ll.appendnode(3)
ll.appendnode(4)
ll.appendnode(5)
ll.printnode()
ll.deleteat(3)
ll.printnode()