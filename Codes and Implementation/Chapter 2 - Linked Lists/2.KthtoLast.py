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

    def kth_element(self,num):
        if num == 0: return None
        Curr_Node=self.head
        for num in range(0,num-1):
            Curr_Node=Curr_Node.next

        while Curr_Node is not None:
            print("(",Curr_Node.data,end=" ) --> ")
            Curr_Node=Curr_Node.next
        print("\n")

ll=LinkedList()

ll.appendnode(1)
ll.appendnode(2)
ll.appendnode(3)
ll.appendnode(4)
ll.appendnode(5)
ll.printnode()
print("Priting from 2 to last element . . .")
ll.kth_element(2)
print("Priting from 4 to last element . . .")
ll.kth_element(4)