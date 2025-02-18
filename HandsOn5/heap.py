# Iftekhar Uddin

class MinHeap:
   
    def __init__(self, data=None):
        self.heap = data if data else []
        if self.heap:
            self.build_min_heap()

    def left(self, i):
        return (i << 1) + 1  # 2 * i + 1

    def right(self, i):
        return (i << 1) + 2  # 2 * i + 2

    def parent(self, i):
        return (i - 1) >> 1  # (i - 1) // 2

    def heapify(self, i):
        smallest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify(smallest)

    def build_min_heap(self):
        for i in range((len(self.heap) - 1) >> 1, -1, -1):
            self.heapify(i)

    def push(self, value):
        self.heap.append(value)
        i = len(self.heap) - 1
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def __str__(self):
        return str(self.heap)

# Demo
if __name__ == "__main__":
    print("Building Min Heap from list [3, 1, 6, 5, 2, 4]:")
    heap = MinHeap([3, 1, 6, 5, 2, 4])
    print("Min Heap:", heap)

    print("Pushing 0 into heap:")
    heap.push(0)
    print("Min Heap:", heap)

    print("Popping the root element:")
    print("Popped element:", heap.pop())
    print("Min Heap:", heap)

    print("Peeking at root element:")
    print("Root element:", heap.peek())
    print("Final Min Heap:", heap)
