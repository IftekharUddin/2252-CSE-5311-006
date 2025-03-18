class Stack:
    def __init__(self, size):
        self.size = size
        self.array = [0] * size  # Fixed-size C-style array
        self.top = -1  # Indicates empty stack

    def push(self, value):
        if self.top == self.size - 1:
            raise OverflowError("Stack overflow")
        self.top += 1
        self.array[self.top] = value

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        value = self.array[self.top]
        self.top -= 1
        return value

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")
        return self.array[self.top]
