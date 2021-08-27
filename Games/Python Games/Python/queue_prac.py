class Queue:
    def __init__(self):
        self.values = []
        self.length = 0

    def add(self, num):
        self.values.append(num)
        self.length += 1

    def remove(self):
        if (len(self.values) == 0):
            return
        self.values.pop(0)  #remove from front of list
        self.length = self.length - 1

    def print(self):
        print(self.values)

    def getLength(self):
    	return self.length
