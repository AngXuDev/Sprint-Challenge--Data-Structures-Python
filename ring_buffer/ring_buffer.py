class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # keep track of current oldest variable in list with current
        # if current is less than length, current is index of next element to delete
        if self.current < self.capacity:
            # when deleting, use current index to delete oldest element
            self.storage.pop(self.current)
            # when inserting new element, insert it where oldest element was just removed
            self.storage.insert(self.current, item)
            # advance current index by 1 to target next oldest element
            self.current = self.current + 1
            print(self.storage)
            # when current reaches end of list, reset to zero to target next oldest element
            if self.current == self.capacity:
                self.current = 0

    def get(self):
        # initiate empty list
        answer = []
        # add to empty list if item is not None
        for i in self.storage:
            if i != None:
                answer.append(i)
        return answer
