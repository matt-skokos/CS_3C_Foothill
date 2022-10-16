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