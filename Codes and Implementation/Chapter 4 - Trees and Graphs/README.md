# Tress

Unlike Arrays, Linked Lists, Stack and queues, which are linear data structures, trees are hierarchical data structures. A tree is with a recursive explanation. A tree is a data structure composed of nodes.

* Each tree has a root node.
* The root node has zero or more child nodes.
* Each node has zero or more child nodes and so on.

> The tree cannot contain cycles. The nodes may or may not be in a particular order, they could have any data type as values, and they may or may not have links back to their parent nodes.

### Creating a simple node in binary tree

To create a simple node in binary tree we need to follow few things.

* Create a root node
* Create a left child
* Create a right child

```python
class Node:
    def __init__(self,val):
        self.root=val
        self.left=None
        self.right=None
```

---

### Creating a simple binary tree

While assigning the value to a binary tree we simply call the fuction and provide the value to it.

```python
root=Node(1)    #will assign to root

root.left=Node(2)     #will assign to left node
root.right=Node(3)    #will assign to right node
```

---

### Types of tress 

1. Full Tree -> Each node have either 2 child node or no node.
2. Complete Tree -> FIll the tree row by row.
3. Perfect Tree -> A perfect tree is both complete and full.

![alt text](https://github.com/AdarshRazor/Cracking_Coding_Interview/blob/main/Codes%20and%20Implementation/Img/1.png "types of trees")

---

### Traversal

1. Preorder traversal -> node | left | right
2. Inorder traversal -> left | node | right
3. Postorder traversal -> left | right | node