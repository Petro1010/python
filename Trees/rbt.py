class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()   # uncle is the brother of the parent, and child of the grandfather

    def uncle_is_black(self):
        if self.get_uncle() == None:    # if no uncle is there, it is considered to be black
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):
        new_root = self.left   # root that will become new root is the left child

        if self.parent != None:    # if node is not the root
            if self.is_left_child():    # if the node is a left child, the new left child will be the new root
                self.parent.left = new_root
            else:
                self.parent.right = new_root   # otherwise, new root is the right child

        self.left = new_root.right    # the left child of the old root becomes the right child of the new root
        if new_root.right != None:     # if new root has a right child
            new_root.right.parent = self
        new_root.right = self   # the right of the new root is the old root
        new_root.parent = self.parent   # parent of the new root is parent of the old root
        self.parent = new_root   #parent of old root is new root

    def rotate_left(self):
        new_root = self.right

        if self.parent != None:
            if self.is_left_child():
                self.parent.left = new_root
            else:
                self.parent.right = new_root

        self.right = new_root.left
        if new_root.left != None:
            new_root.left.parent = self
        new_root.left = self
        new_root.parent = self.parent
        self.parent = new_root


class RBTree:

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
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def get_number_of_nodes(self):
        if self.is_empty():
            return 0
        return self.__get_number_of_nodes(self.root)

    def __get_number_of_nodes(self, node):
        if node == None:
            return 0
        return 1 + self.__get_number_of_nodes(node.left) + self.__get_number_of_nodes(node.right)

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        if node.parent == None:  #root should always be black
            node.make_black()
        while node != None and node.parent != None and node.parent.is_red():  # If the parent node is red, node must have a grandparent
            uncle = node.get_uncle()
            if uncle != None and uncle.is_red():   #if uncle is red, and parent is parent is red, make both black and make grand parent red
                node.parent.make_black()
                node.parent.parent.make_red()
                if uncle != None:
                    uncle.make_black()
                node = node.parent.parent   # fix from the grandparent
            elif node.parent.is_left_child():   #if parent is left child
                if node.is_right_child():  #if node is right child, rotate left and update parent appropriately
                    node = node.parent
                    node.rotate_left()
                node.parent.make_black()
                node.parent.parent.make_red()
                node.parent.parent.rotate_right() #if node is left child, just rotate right
            else:  # Parent is right child
                if node.is_left_child():   #if node is left child, rotate right before rotating left
                    node = node.parent
                    node.rotate_right()
                node.parent.make_black()
                node.parent.parent.make_red()
                node.parent.parent.rotate_left()
        while self.root.parent != None:
            self.root = self.root.parent
        self.root.make_black()

    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" + self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"

    def __repr__(self):
        return self.__str__()