import math

# Hash functions

def multiplication_hash(key, size):
    A = (math.sqrt(5) - 1) / 2
    return int(size * ((key * A) % 1))

def division_hash(key, size):
    return key % size

# Doubly linked list node
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Doubly linked list for chaining
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, key, value):
        node = Node(key, value)
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node

    def delete(self, key):
        current = self.head
        while current:
            if current.key == key:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return True
            current = current.next
        return False

    def search(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def items(self):
        current = self.head
        while current:
            yield (current.key, current.value)
            current = current.next

    def is_empty(self):
        return self.head is None

class HashTable:
    def __init__(self, initial_capacity=8, hash_func=multiplication_hash):
        self.capacity = initial_capacity
        self.size = 0
        self.hash_func = hash_func
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]

    def _resize(self, new_capacity):
        old_items = [(key, val) for bucket in self.buckets for key, val in bucket.items()]
        self.capacity = new_capacity
        self.buckets = [DoublyLinkedList() for _ in range(self.capacity)]
        self.size = 0
        for key, value in old_items:
            self.insert(key, value)

    def insert(self, key, value):
        index = self.hash_func(key, self.capacity)
        bucket = self.buckets[index]
        if bucket.search(key) is None:
            self.size += 1
        else:
            bucket.delete(key)  # Replace existing key
        bucket.insert(key, value)
        if self.size >= self.capacity:
            self._resize(self.capacity * 2)

    def delete(self, key):
        index = self.hash_func(key, self.capacity)
        bucket = self.buckets[index]
        if bucket.delete(key):
            self.size -= 1
            if self.size <= self.capacity // 4 and self.capacity > 8:
                self._resize(self.capacity // 2)

    def search(self, key):
        index = self.hash_func(key, self.capacity)
        return self.buckets[index].search(key)

    def display(self):
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}:", list(bucket.items()))

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    for i in range(20):
        ht.insert(i, i*10)
    ht.display()
    for i in range(10):
        ht.delete(i)
    ht.display()
    print("Search key 15:", ht.search(15))
