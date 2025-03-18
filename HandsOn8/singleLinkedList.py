class SinglyLinkedList:
    def __init__(self, size):
        self.size = size
        self.array = [[None, None] for _ in range(size)]  # Each element stores [data, next_index]
        self.head = None
        self.free = list(range(size))  # Free index pool

    def insert(self, value):
        if not self.free:
            raise OverflowError("Linked list memory full")
        new_index = self.free.pop(0)
        self.array[new_index] = [value, None]  # Store data and next pointer
        if self.head is None:
            self.head = new_index
        else:
            current_index = self.head
            while self.array[current_index][1] is not None:
                current_index = self.array[current_index][1]
            self.array[current_index][1] = new_index

    def delete(self, value):
        prev_index = None
        current_index = self.head
        while current_index is not None:
            node_data, next_index = self.array[current_index]
            if node_data == value:
                if prev_index is None:
                    self.head = next_index  # Removing head
                else:
                    self.array[prev_index][1] = next_index
                self.free.append(current_index)  # Free this slot
                return
            prev_index = current_index
            current_index = next_index
        raise ValueError("Value not found in list")

    def search(self, value):
        current_index = self.head
        while current_index is not None:
            if self.array[current_index][0] == value:  # Access data at index
                return current_index
            current_index = self.array[current_index][1]  # Move to the next index
        return None  # Value not found

    def display(self):
        current_index = self.head
        result = []
        while current_index is not None:
            result.append(self.array[current_index][0])  # Collect data at index
            current_index = self.array[current_index][1]  # Move to the next index
        return result  # Return the list representation
