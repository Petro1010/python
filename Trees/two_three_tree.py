#2-3 tree:
import random

class TwoThreeNode:

    def __init__(self, value):
        self.values = [value]
        self.children = [None, None, None, None]  #the biggest a node can get is a 4 node, with a maximum of 4 children
        self.parent = None

    def is_leaf(self):
        return self.children[0] == None     #is a leaf if it does not have a child

    def is_two_node(self):
        return len(self.values) == 1   #2 node if node has one value

    def is_three_node(self):
        return len(self.values) == 2   #3 node if node has 2 values

    def add_to(self, value):   #append the value to the node, and make sure that it is sorted (smallest on left)
        self.values.append(value)
        self.values.sort()

    def __str__(self):
        if self.is_leaf():
            if self.is_two_node():
                return "[" + str(self.values[0]) + "]"
            else:
                return "[" + str(self.values[0]) + " " + str(self.values[1]) + "]"
        else:
            if self.is_two_node():
                return "[" + str(self.children[0]) + str(self.values[0]) + str(self.children[1]) + "]"
            else:
                return "[" + str(self.children[0]) + str(self.values[0]) + str(self.children[1]) + str(
                    self.values[1]) + str(self.children[2]) + "]"

    def __repr__(self):
        return self.__str__()


class TwoThreeTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        if node.is_leaf():
            return 1
        if node.is_two_node:
            return 1 + max(self.__get_height(node.children[0]), self.__get_height(node.children[1]))   #case for 2 nodes
        return 1 + max(self.__get_height(node.children[0]), self._get_height(node.children[1]), self.__get_height(node.children[2]))  #case for 3 nodes

    def insert(self, value):
        if self.is_empty():
            self.root = TwoThreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if node.is_leaf():        #only adds value to a node if it is at the bottom of the tree (is a leaf)
            if node.is_two_node():
                node.add_to(value)
            else:  # Is a 3 node, adding to a 3 node will create a 4 node and an error that must be fixed
                node.add_to(value)
                self.fix(node)
        elif node.is_two_node():     #if its a two node
            if value < node.values[0]:     #if its less than the node, go left
                self._insert(value, node.children[0])
            else:  #if its more than node, go right
                self._insert(value, node.children[1])
        else:  # Is a 3 node
            if value < node.values[0]:    #if its less than first node go left
                self._insert(value, node.children[0])
            elif value < node.values[1]:   #if its less than second node, but greater than first node, go mid
                self._insert(value, node.children[1])
            else:  #if its greater than both nodes, go right
                self._insert(value, node.children[2])

    def fix(self, node):   #If we reach this case, we have a 4 node

        if node.parent != None:    #if the 4 node is not in the root
            mid_value = node.values[1]
            new1 = TwoThreeNode(node.values[0])
            new2 = TwoThreeNode(node.values[2])
            new1.children[0] = node.children[0]   #transfering over the children
            new1.children[1] = node.children[1]
            if not node.is_leaf():
                node.children[0].parent = new1   #linking children back to parents
                node.children[1].parent = new1
            new1.parent = node.parent            #parent of new node is parent of old node

            new2.children[0] = node.children[2]
            new2.children[1] = node.children[3]
            if not node.is_leaf():
                node.children[2].parent = new2
                node.children[3].parent = new2
            new2.parent = node.parent
            if node.parent.is_three_node():   #if the parent is a three node, this will result in another 4 node, need to update its children
                node.parent.add_to(mid_value)
                if node == node.parent.children[0]:  #node is the left child
                    node.parent.children = [new1] + [new2] + node.parent.children[1:3]
                elif node == node.parent.children[1]:    #node is mid child
                    node.parent.children = [node.parent.children[0]] + [new1] + [new2] + [node.parent.children[2]]
                else:  #node is right child
                    node.parent.children = node.parent.children[:2] + [new1] + [new2]
                self.fix(node.parent)   #once children are updated, fix it
            else:  # Is a two node, do not need to worry about fix
                node.parent.add_to(mid_value)
                if node == node.parent.children[0]:    #if node is left child
                    node.parent.children = [new1] + [new2] + [node.parent.children[1]]
                else:  #if node is right child
                    node.parent.children = [node.parent.children[0]] + [new1] + [new2]
        else:  # Root needs to split
            mid_value = node.values[1]
            new_root = TwoThreeNode(mid_value)
            new1 = TwoThreeNode(node.values[0])
            new2 = TwoThreeNode(node.values[2])
            new1.children[0] = node.children[0]
            new1.children[1] = node.children[1]
            if not node.is_leaf():
                node.children[0].parent = new1
                node.children[1].parent = new1
            new1.parent = new_root
            new2.children[0] = node.children[2]
            new2.children[1] = node.children[3]
            if not node.is_leaf():
                node.children[2].parent = new2
                node.children[3].parent = new2
            new2.parent = new_root
            new_root.children[0] = new1
            new_root.children[1] = new2
            self.root = new_root

    def __str__(self):
        if self.is_empty():
            return "[]"
        return str(self.root)

    def __repr__(self):
        if self.is_empty():
            return "[]"
        return str(self.root)