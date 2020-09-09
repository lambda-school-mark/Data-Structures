"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        added = ListNode(value)
        if self.length == 0:
            self.head = added
            self.tail = added
        else:
            self.head.prev = added
            added.next = self.head
            self.head = added
        self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        if self.length == 0:
            return None

        removed = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return removed.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        added = ListNode(value)
        if self.length == 0:
            self.head = added
            self.tail = added
        else:
            self.tail.next = added
            added.prev = self.tail
            self.tail = added
        self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.length == 0:
            return None

        removed = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return removed.value

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        moved = node
        if moved is self.tail:
            if self.length == 2:
                self.tail.prev.next = None
                self.tail = self.tail.prev
                self.head.prev = moved
                moved.next = self.head
                self.head = moved
            else:
                self.head.next = None
                self.tail.prev = None
                self.tail = self.head
                self.head = moved
        else:
            moved.next.prev = moved.prev
            moved.prev.next = moved
            self.head.prev = moved
            moved.next = self.head
            self.head = moved

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        moved = node
        if moved is self.head:
            if self.length == 2:
                self.head.next.prev = None
                self.head = self.head.next
                self.tail.next = moved
                moved.prev = self.tail
                self.tail = moved
            else:
                self.tail.prev = None
                self.head.next = None
                self.head = self.tail
                self.tail = moved
        else:
            moved.prev.next = moved.next
            moved.next.prev = moved
            self.tail.next = moved
            moved.prev = self.tail
            self.tail = moved

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        removed = node
        if removed is self.head:
            self.head = self.head.next
        if removed is self.tail:
            self.tail = self.tail.prev
        if removed.prev:
            removed.prev.next = removed.next
        if removed.next:
            removed.next.prev = removed.prev
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        current = self.head
        maximum = current.value
        while current.next != None:
            current = current.next
            if current.value > maximum:
                maximum = current.value
        return maximum
