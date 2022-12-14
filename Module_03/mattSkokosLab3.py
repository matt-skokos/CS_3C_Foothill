"""
Matt Skokos
Assignment 3 - Linked Lists and Stacks

This project will implement a node class, a stack class and the related
methods to create and manipulate them.
"""


class Node:
    validParamList = "(){}[]"

    def __init__(self, value):
        self.value = value
        self.next = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    def setValue(self, newValue):
        if isinstance(newValue, str) and \
                newValue in Node.validParamList:
            self.value = newValue

    def setNext(self, newNext):
        if isinstance(newNext, str) and \
                newNext in Node.validParamList:
            self.next = newNext

    @staticmethod
    def validateParameter(node):
        """ Validate parameter data. """
        return node.value in Node.validParamList

    @staticmethod
    def checkNodeNext(node):
        """ Validate that the next """
        return node.next is not None


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
