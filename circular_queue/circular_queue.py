# Write your code here to make the tests pass.
#
# Change your working directory to this directory,
# circular_queue.
#
# # Start by running python -m pytest tests/test_01.py and
# making the test pass.
#
# Then, run python -m pytest tests/test_02.py to make the
# next test pass. Keep going to tests/test_XX.py.

class CircularQueue:
    def __init__(self, size, head=0, tail=0):
        self.size = size
        self.head = head
        self.tail = tail
        self.buffer = [None] * size
        self.length = 0

    def dequeue(self):
        val = self.buffer[self.head]
        self.length -= 1
        self.head += 1
        return val


    def enqueue(self, val):

        self.length += 1
        self.tail += 1


        for index, value in enumerate(self.buffer):
            if value is None:
                self.buffer[index] = val
                break
        for value in self.buffer:
            if value is None:
                break
            else:
                self.head = 0
                self.tail = 0
