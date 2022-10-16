class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[:-1]

    def isEmpty(self):
        return self.stack == []

    @classmethod
    def createStack(self, name):
        name = Stack()

    def deleteStack(self, name):
        name.clear()
