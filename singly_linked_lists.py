class SList:
    def __init__(self):
        self.head = None
    def addtoFront(self, val):
        newNode = SNode(val)
        current_head = self.head
        newNode.next = current_head
        self.head = newNode
        return self
    
    def addtoBack(self, val):
        if self.head == None:
            self.addtoFront(val)
            return self
        newNode = SNode(val)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = newNode
        return self
    def printValues(self):
        runner = self.head
        while(runner != None):
            print(runner.val)
            runner = runner.next
        return self

class SNode:
    def __init__(self, val):
        self.val = val
        self.next = None

myList = SList()
myList.addtoFront(5).addtoFront(6).addtoBack(12).addtoFront(34)
myList.printValues()