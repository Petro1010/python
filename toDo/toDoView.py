class View:

    def __init__(self, todo):
        self.todo = todo

    def viewList(self):
        print("---------------TO DO---------------")
        if self.todo.root is not None:
            curr = self.todo.root
            ind = 1
            while(curr.next != None):
                print(f"({ind}) {curr.task} | Priority: {curr.pri}")
                curr = curr.next
                ind += 1
			
            print(f"({ind}) {curr.task} | Priority: {curr.pri}")
        print("-----------------------------------")
    
    def unusedPriorities(self):
        print(f"Missing priorities include: {self.todo.missingPri()}")
    
    def startUp(self):
        print("What would you like to do?: (1) View List (2) Add Task (3) Delete Task (4) Exit")
    
    def error(self):
        print("--Invalid input, please try again!--")
    
    def add1(self):
        print("Enter task: ")
    
    def add2(self):
        print("Enter priority of task: ")
    
    def addComplete(self):
        print("Add successful!")

    def delete(self):
        print("Enter task to delete: ")
    
    def deleteComplete(self):
        print("Delete successful!")
    
    def noDelete(self):
        print("--Can not delete from empty list!--")

