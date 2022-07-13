class Node:
    # This is a main node class for linked list
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head = None
    tail = None
    size = 0

    def add_first(self, value):
        node = Node(value)

        # If node is empty then head and tail will be the newly created node
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            # If head not is not empty then head will be moved to new node and previous head will point to the next node
            current_node = self.head
            self.head = current_node
            self.head.next = current_node

        self.size += 1

    def add_last(self, value):
        node = Node(value)

        # If node is empty then head and tail will be the newly created node
        if(self.head is None):
            self.head = node
            self.tail = node
        else:
            # If tail is not empty then tail will be moved to new node and previous node next will point to new tail
            self.tail.next = node
            self.tail = self.tail.next

        self.size += 1

    def search(self, value):
        current_index = 0
        current_node = self.head

        while(current_node is not None):
            if(current_node.value == value):
                print("Item Found {}".format(str(current_index)))
                return
            else:
                current_node = current_node.next
            current_index += 1

        print("Item not found")

    def delete_first(self):
        # If head is empty then return a message
        if(self.head is None):
            print("No item is found in list")
            return

        # If list has only one item
        if(self.head.next is None):
            self.head = None
            self.tail = None
            return

        # Otherwise move head to next item and previous will become garbage
        self.head = self.head.next

        self.size -= 1

    def delete_last(self):
        # If head is empty then return a message
        if(self.head is None):
            print("No item is found in list")
            return

        # If list has only one item
        if(self.head.next is None):
            self.head = None
            self.tail = None
            return

        # Otherwise move tails to previous item and next will become garbage
        current_node = self.head
        second_current_node = self.head.next

        while(current_node.next is not None):
            if(second_current_node.next.next is None):
                self.tail = second_current_node
                second_current_node.next = None
                return
            current_node = current_node.next
            second_current_node = second_current_node.next.next
        self.size -= 1

    def print_values(self):
        # If head is empty then return a message
        if(self.head is None):
            print("No item is found in list")
            return

        current_node = self.head

        print("Values:", end=" ")

        while(current_node is not None):
            print("{}".format(str(current_node.value)), end=" ")
            current_node = current_node.next
        print("")


if __name__ == "__main__":
    # Use Linked List
    ll = LinkedList()

    # Add Item
    ll.add_first(4)
    ll.add_last(10)
    ll.add_last(5)
    ll.add_last(12)
    ll.add_last(15)
    ll.add_last(20)
    ll.print_values()

    # Search Item
    ll.search(10)
    ll.search(40)

    # Delete Item
    ll.delete_first()
    ll.delete_last()
    ll.print_values()
