from toDoListModel import ToDoList
from toDoView import View
from toDoController import Controller

todoList = ToDoList()
view = View(todoList)
control = Controller(todoList, view)

control.start()