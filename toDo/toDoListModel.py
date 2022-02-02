class Item:
    def __init__(self, task, priority):
        self.task = task
        self.pri = priority
        self.next = None

class ToDoList:

    def __init__(self):
        self.root = None
        self.len = 0
        self.currentPri = []

    def add(self, item):
        self.currentPri.append(item.pri)
        self.len += 1
        if self.root is None: #TodoList is empty
            self.root = item
        
        else:
            if self.root.pri >= item.pri: #case for when new item is highest priority
                item.next = self.root
                self.root = item

            else:
                curr = self.root
                while curr.next != None:
                    if curr.next.pri >= item.pri: #insert at correct priority
                        item.next = curr.next
                        curr.next = item
                        return
                    curr = curr.next
                
                curr.next = item  #if priority is last

    def delete(self, ind):
        self.len -= 1
        if ind == 1: #delete first node
            self.currentPri.remove(self.root.pri)
            self.root = self.root.next
        
        else:
            node = 1
            curr = self.root

            while node != ind - 1:  #get to node before position to be deleted
                curr = curr.next
                node += 1

            self.currentPri.remove(curr.next.pri)
            curr.next = curr.next.next #delete the node
    
    def missingPri(self):
        if self.root is None:
            return []
        return list(set([i for i in range(1, max(self.currentPri) + 1)]).difference(set(self.currentPri))) #the set difference between possible and current priorities
    
    #def print(self):
        #if (len(self.currentPri) == 0):
            #print("[]")
		
        #else:
            #s = "["
            #current = self.root
            #while(current.next != None):
                #s += str(current.pri) + " -> "
                #current = current.next
			
            #s+= str(current.pri) + "]"
            #print(s)