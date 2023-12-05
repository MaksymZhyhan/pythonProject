# Task1

class UnsortedList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def index(self, item):
        try:
            self.items.index(item)
        except ValueError:
            raise ValueError(f"{item} not found in the list")

    def pop(self, index=-1):
        try:
            return self.items.pop(index)
        except IndexError:
            raise IndexError("pop from an empty list")

    def insert(self, index, item):
        self.items.insert(index, item)

    def slice(self, start, stop):
        return self.slice[start:stop]


my_list = UnsortedList()


# Task2


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Task3


class Node2:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from an empty queue")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return dequeued_data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty queue")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
