# Linked Lists

Linear Data Structure { Not stored at a contigeous location}.
Elements are linked using pointers and linked to one another.

> This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements. 

### Creating the Simple linked list

To create a linked list we just need to follow few things.

* Create a class node and assign the data and next.
* Create a append class and assign the head to temp.
* Itterate the next till it gets null.
* Add the node in the last.
* To append a node, simply pass the data value to the class and putting next to null.

> Inseting at beg O(1). Inserting at end O(n).

### Deleting a Node 

We find the previous node *prev* and set *prev.next* equal to *n.next*. 

If the list is doubly linked, we must also update *n.next* to set *n.next.prev* equal to *n.prev*. 