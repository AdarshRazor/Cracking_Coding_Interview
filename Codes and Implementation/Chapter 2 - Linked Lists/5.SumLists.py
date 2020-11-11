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
        
    def conv(self):
        curr_node=self.head
        string=""
        while curr_node is not None:
            string+=str(curr_node.data)
            curr_node=curr_node.next
        string=int(string)
        return(string)

def adding_sum(num,num2):
    return(num+num2)

ll=LinkedList()
ll2=LinkedList()

for i in range(1,4):
    ll.appendnode(i)
ll.printnode()
print(ll.conv())

for i in range(4,7):
    ll2.appendnode(i)
ll2.printnode()
print(ll2.conv())

result=str(adding_sum(ll.conv(),ll2.conv()))
print("\nSum of",ll.conv(),"and",ll2.conv(),"is: ",result,"\n")

ll3=LinkedList()
for i in range(len(result)):
    ll3.appendnode(result[i])
ll3.printnode()