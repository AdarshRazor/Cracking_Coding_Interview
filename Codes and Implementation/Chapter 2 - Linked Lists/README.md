# Linked Lists

Linear Data Structure { Not stored at a contigeous location}.
Elements are linked using pointers and linked to one another.

> This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements. 

---

### Creating the Simple linked list

To create a linked list we just need to follow few things.

* Create a class node and assign the data and next.
* Create a append class and assign the head to temp.
* Itterate the next till it gets null.
* Add the node in the last.
* To append a node, simply pass the data value to the class and putting next to null.

> Inseting at beg O(1). Inserting at end O(n).

```python
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

ll=LinkedList()

ll.appendnode(9)
ll.appendnode(7)
ll.appendnode(2)
ll.printnode()
```

---

### Deleting a Node 

To delete the node from the linked list.

* We find the previous node **prev** and set **prev.next** equal to **n.next**. 
* If the list is doubly linked, we must also update **n.next** to set **n.next.prev** equal to **n.prev**. 

> Deleting from beg O(1). Deleting from anywhere in the linekd O(n).

---

### The Runner Technique

The **"runner"** (or second pointer) technique is used in many linked list problems. The runner technique
means that you iterate through the linked list with two pointers simultaneously, with one ahead of the
other. The **"fast"** node might be ahead by a fixed amount, or it might be hopping multiple nodes for each
one node that the **"slow"** node iterates through.

for more please refere the [book](https://www.amazon.in/Cracking-the-Coding-Interview/dp/0984782869/ref=sr_1_1_sspa?crid=143LZWU680S2S&dchild=1&keywords=cracking+coding+interview&qid=1604287328&sprefix=ipad+8th+ge%2Caps%2C505&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFBOEtTR0tNU1haNlMmZW5jcnlwdGVkSWQ9QTAyODUyOTczNkY1Uk9MMkNTUkw5JmVuY3J5cHRlZEFkSWQ9QTA2MDY5OTAzT1FXRTNPWlNBUVRDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)

---

### Recursive Method

We can do the linked list problems using recursion also. 
> Recursive algorithms take at least O(n) space, where n is the depth of the recursive call. 
All recursive algorithms can be implemented iteratively, although they may be much more complex. 

