"""
Matt Skokos
Assignment 3 - Linked Lists and Stacks

This project will implement a node class, a stack class and the related
methods to create and manipulate them.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newValue):
        self.value = newValue

    def setNext(self, newNext):
        self.next = newNext

class Stack:
    def __init__(self):
        self.head = Node("head")
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


def main():
    pass