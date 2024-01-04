class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit




    def isEmpty(self):
        for item in self.items:
            if item.isEmpty:
                return False
            else:
                return True
        pass

    def push(self, item):
        self.items.append(item)
        pass

    def pop(self):
        pass
        

    def peek(self):

        pass
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    
    def size(self):
        pass
        return len(self.items) 

    def full(self):

        pass
        return len(self.items) >= self.limit

    def search(self, target):

        pass
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
