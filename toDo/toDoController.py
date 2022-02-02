from toDoListModel import Item
class Controller:

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.startUp()
        choice = input()

        if choice == "1":
            self.show()

        elif choice == "2":
            self.addTask()
        
        elif choice == "3":
            self.deleteTask()
        
        elif choice == "4":
            return
        
        else:
            self.view.error()
            print()
            self.start()
    
    def show(self):
        self.view.viewList()
        self.view.unusedPriorities()
        print()
        self.start()
    
    def addTask(self):
        self.view.add1()
        task = input()
        print()
        self.view.add2()
        try:
            pri = int(input())
            print()
            if pri > 0: #ensure positive int as priority
                self.model.add(Item(task, pri))
                self.view.addComplete()
                print()
                self.start()
            else:
                self.view.error()
                print()
                self.addTask()
        
        except ValueError:
            print()
            self.view.error()
            print()
            self.addTask()

    
    def deleteTask(self):
        if self.model.len == 0: #ensure no deletion on empty list
            self.view.noDelete()
            print()
            self.start()
        
        else:
            self.view.viewList()
            self.view.delete()
            try:
                delete = int(input())
                if delete > 0 and delete <= self.model.len: #delete node within list
                    self.model.delete(delete)
                    print()
                    self.view.deleteComplete()
                    print()
                    self.start()
                else:
                    print()
                    self.view.error()
                    print()
                    self.deleteTask()

            except ValueError:
                print()
                self.view.error()
                print()
                self.deleteTask()