from collections import deque

class Queue:
    def __init__(self):
        self.data = deque()

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        return self.data.popleft()

    def search(self, index):
        if (0 <= index < len(self)):
            return self.data[index]

        raise IndexError

