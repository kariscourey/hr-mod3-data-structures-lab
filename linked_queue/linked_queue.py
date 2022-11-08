# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# linked_queue.
#
# # Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_15.py.

class LinkedQueueNode:
    def __init__(self, value=None, link=None):
        self.value = value
        self.link = link

class LinkedQueue:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def dequeue(self):
        if self.head.link is None:
            val = self.head.value
            self.head, self.tail = None, None
            return val

        val = self.head.value
        self.head = self.head.link
        return val

    def enqueue(self, val):

        node = LinkedQueueNode(val)

        if self.head is None:
            self.head = node
            self.tail = node
            return None

        self.tail.link = node
        self.tail = node
        return None
