from Estructuras.LinkedList import LinkedList

class HashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [LinkedList() for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]
        
        # If the key already exists, update the value
        current = bucket.head
        while current:
            k, _ = current.data
            if k == key:
                current.data = (key, value)
                return
            current = current.next

        # If key doesn't exist, append new node
        bucket.add((key, value))
        self.size += 1

    def get(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        
        while current:
            k, v = current.data
            if k == key:
                return v
            current = current.next
        
        return None # Si no se encuentra regresa None

    def delete(self, key):
        index = self._hash(key)
        bucket = self.buckets[index]
        current = bucket.head
        position = 0

        while current:
            k, _ = current.data
            if k == key:
                print(position)
                bucket.remove_at(position)
                self.size -= 1
                return
            current = current.next
            position += 1

        raise KeyError(f"Key '{key}' not found")

    def __repr__(self):
        result = ""
        for i in range(self.capacity):
            result += f"[{i}]: {self.buckets[i]}\n"
        return result
