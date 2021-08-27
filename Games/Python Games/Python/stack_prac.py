class Stack:
    def __init__(self):
        self.values = []
        self.height = 0
  
    def push(self,num):
        self.values.append(num)
        self.height = self.height + 1

    def pop(self):
        if (len(self.values) == 0):
            return
        self.values.pop(len(self.values) - 1)  #remove from back of list
        self.height = self.height - 1


    def print(self):
        print(self.values)

    def getHeight(self):
    	return self.height

    def isEmpty(self):
    	return len(self.values) == 0



stack = Stack()
stack.print()

stack.push(3)
stack.print()
print(stack.getHeight())

stack.pop()
stack.pop()
stack.print()	
stack.push(3)
stack.push(4)
stack.push(88)
stack.push(100)
stack.print()

stack.pop()
stack.print()

print(stack.isEmpty())
stack.pop()
stack.pop()
stack.pop()
print(stack.isEmpty())
