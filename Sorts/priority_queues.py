#Priority Queue implementations

#implementation with unordered list
class Pri_Queue_unordered():

    def __init__(self):
        self.data = []

    def insert(self, value):
        self.data.append(value)

    def remove_max(self):
        if len(self.data) == 0:
            return
        maxindex = 0
        for i in range(len(self.data)):
            if self.data[i] > self.data[maxindex]:
                maxindex = i

        del self.data[maxindex]

    def find_max(self):
        maxindex = 0
        for i in range(len(self.data)):
            if self.data[i] > self.data[maxindex]:
                maxindex = i

        return self.data[maxindex]

    def print(self):
        print(self.data)

#implementation with ordered list

class Pri_Queue_ordered():

    def __init__(self):
        self.data = []

    def insert(self, value):
        if len(self.data) == 0 or value > self.data[-1]:
            self.data.append(value)
        elif value < self.data[0]:
            self.data.insert(0, value)
        else:
            for i in range(len(self.data)):
                if value >= self.data[i] and value <= self.data[i + 1]:
                    self.data.insert(i + 1, value)
                    break

    def remove_max(self):
        self.data.pop()

    def find_max(self):
        return self.data[-1]

    def print(self):
        print(self.data)

#implementation with max heap

class Pri_Queue_heap():

    def __init__(self, lst):
        self.data = lst
        self.length = len(lst)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[largest_known]: #if left child is bigger make note of it
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]: #if right child is bigger than left make note of it
            largest_known = self.right(i)
        if largest_known != i: #if i is smaller than its children then swap it
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)   #continue sinking largest known value

    def swim(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def remove_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1  # that value hasnt actually been removed, but the program no longer recognizes it
        self.sink(0)
        return max_value

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

#implementation of min heap

class Pri_Queue_heap2():

    def __init__(self, lst):
        self.data = lst
        self.length = len(lst)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] < self.data[smallest_known]:  # if left child is bigger make note of it
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] < self.data[smallest_known]:  # if right child is bigger than left make note of it
            smallest_known = self.right(i)
        if smallest_known != i:  # if i is smaller than its children then swap it
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.sink(smallest_known)  # continue sinking largest known value

    def swim(self, i):
        while i > 0 and self.data[i] < self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def remove_min(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        min_value = self.data[self.length - 1]
        self.length -= 1  # that value hasnt actually been removed, but the program no longer recognizes it
        self.sink(0)
        return min_value

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.swim(self.length - 1)

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s