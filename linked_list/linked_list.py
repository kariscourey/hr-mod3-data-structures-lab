# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# linked_list.
#
# Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_19.py.


class LinkedListNode:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    # @property
    # def length(self):
    #     return self.length

    def get(self, index):

        current_node = self.head
        i = 0
        while current_node is not None:
            current_node = current_node.link
            i += 1
        if index < 0:
            index += i


        current_node = self.head
        i = 0

        while current_node is not None:
            if i == index:
                return current_node.value
            current_node = current_node.link
            i += 1
        raise IndexError


    def insert(self, val, index=None):
        node = LinkedListNode(val)

        if self.head is None:
            self.head = node
            self.tail = node
            self.length += 1
            return None

        elif index is None:
            self.tail.link = node
            self.tail = node
            self.length += 1
            return None

        elif index == 0:
            node.link = self.head
            self.head = node
            self.length += 1
            return None

        current_node = self.head
        i = 0

        while current_node is not None:
            if i == index - 1:
                next_node = current_node.link
                node.link = next_node
                current_node.link = node
                return None
            current_node = current_node.link
            i += 1
        return None



    def remove(self, index):

        if index == 0:
            val = self.head.value
            self.head = self.head.link
            self.length -= 1
            return val

        current_node = self.head
        i = 0

        while i <= index + 1:
            if i == index - 1:
                before_idx_node = current_node
                remove_node = before_idx_node.link
                val = remove_node.value
            elif i == index + 1:
                after_idx_node = current_node
                before_idx_node.link = after_idx_node
                self.length -= 1
                return val
            elif i == index and current_node.link is None:
                before_idx_node.link = current_node
                self.tail = before_idx_node
                self.length -= 1
                return val
            current_node = current_node.link
            i += 1
