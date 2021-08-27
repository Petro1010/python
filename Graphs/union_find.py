#union find:
class UnionFind:

    def __init__(self, values):
        self.parents = {}
        self.size = {}
        for value in values:
            self.parents[value] = value
            self.size[value] = 1

    def find(self, value):
        if self.parents[value] == value:
            return value   #value is root of the set

        self.parents[value] = self.find(self.parents[value]) #
        return self.find(self.parents[value])

    def union(self, value1, value2):
        if self.find(value1) == self.find(value2):
            return  #they are in the same set, do nothing
        else:
            root1 = self.find(value1)
            root2 = self.find(value2)
            #the smaller tree should be hooked up to the big tree

            if self.size[root1] >= self.size[root2]:
                self.parents[root2] = root1   #the parent of root2 is now root1, they are connected
                self.size[root1] += self.size[root2]
            else:
                self.parents[root1] = root2
                self.size[root2] += self.size[root1]