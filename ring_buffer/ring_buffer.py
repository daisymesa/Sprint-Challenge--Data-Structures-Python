from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):

        # if ring buffer is empty, add item to head
        if self.storage.length == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head

        # if ring buffer is not full, add item to tail
        elif self.capacity > self.storage.length:
            self.storage.add_to_tail(item)

        # if ring buffer is full, replace item
        elif self.capacity == self.storage.length:

            if self.current.next is not None:
                self.current.value = item
                self.current = self.current.next

            else:
                self.current.value = item
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        node = self.storage.head
        while node is not None:
            list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
