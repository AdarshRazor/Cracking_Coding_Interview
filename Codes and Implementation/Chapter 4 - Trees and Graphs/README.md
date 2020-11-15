# Tress

Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical data structures. A tree is with a recursive explanation. A tree is a data structure composed of nodes.

* Each tree has a root node.
* The root node has zero or more child nodes.
* Each node has zero or more child nodes and so on.

> The tree cannot contain cycles. The nodes may or may not be in a particular order, they could have any data type as values, and they may or may not have links back to their parent nodes.

### Creating a simple node in binary tree

```python
class Node:
    def __init__(self,val):
        self.root=val
        self.left=None
        self.right=None
```

---

### Creating a simple binary tree

```python
root=Node(1)    #will assign to root

root.left=Node(2)     #will assign to left node
root.right=Node(3)    #will assign to right node
```

---
