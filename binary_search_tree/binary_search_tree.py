"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        new_node = BSTNode(value)

        # If value is greater than node
        if value >= self.value:
            # Then if there no node to the right
            if self.right == None:
                # Create new node
                self.right = new_node
            else:
                # If there is a node, insert the new value
                self.right.insert(value)
        # If value is smaller than node
        if value < self.value:
            # Then if there no node to the left
            if self.left == None:
                # Create new node
                self.left = new_node
            else:
                # If there is a node, insert the new value
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # Look through the right since it contains max value
        # If there is no node to the right
        if self.right == None:
            # Return the max value
            return self.value
        else:
            # Otherwise keep searching right max value
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        # Get value
        fn(self.value)

        # If anything to the right
        if self.right:
            # Recurse and get its value
            self.right.for_each(fn)
        # If anything to the left
        if self.left:
            # Recurse and get its value
            self.left.for_each(fn)

    # * Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):

        # If left node exists, keep going
        if self.left:
            self.left.in_order_print()

        # Print (each) value
        print(self.value)

        # If right node exists, keep going
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self):
        # Call queue
        queue = Queue()

        current_node = self
        # Grab starting node and put it in the queue
        queue.enqueue(current_node)

        # If there are items in the queue
        while queue.size > 0:
            # dequeue the current node
            current_node = queue.dequeue()
            # print the nodes value
            print(current_node.value)

            # check if left child exists
            if current_node.left is not None:
                # enqueue left child
                queue.enqueue(current_node.left)
            # check if right child exists
            if current_node.right is not None:
                # enqueue right child
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        stack = Stack()

        current_node = self

        # Grab starting node and put it in the stack
        stack.push(current_node)

        # If there are items in the stack
        while stack.size > 0:
            # pop the current node
            current_node = stack.pop()
            # print visited
            print(current_node.value)
            # check left
            if current_node.left is not None:
                # push left
                stack.push(current_node.left)
            # check right
            if current_node.right is not None:
                # push right
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # Preorder (Root, Left, Right)
    def pre_order_dft(self):
        # Get root node first
        print(self.value)
        # check if there is a left child node
        if self.left is not None:
            # continue through left and print it (recursive)
            self.left.pre_order_dft()
        # check if there is a right child node
        if self.right is not None:
            # continue through right and print it (recursive)
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    # Postorder (Left, Right, Root)
    def post_order_dft(self):
        # check if there is a left child node
        if self.left is not None:
            # continue through left and print it
            self.left.post_order_dft()
        # check if there is a right child node
        if self.right is not None:
            # continue through right and print it
            self.right.post_order_dft()
        # call function on root node's value last
        print(self.value)


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
