class Queue:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size
        self.head = 0  # Front of the queue
        self.tail = 0  # Next available position
        self.count = 0  # Number of elements in queue

    def enqueue(self, value):
        if self.count == self.size:
            raise OverflowError("Queue overflow")
        self.array[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue underflow")
        value = self.array[self.head]
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return value

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size