class MyHashSet:

    def __init__(self):
        self.p = 1007
        self.container = [None] * self.p

    def add(self, key: int) -> None:
        index = key % self.p
        if self.container[index] is None:
            self.container[index] = []

        if not self.contains(key):
            self.container[index].append(key)
        
    def remove(self, key: int) -> None:
        index = key % self.p
        if self.container[index] is None:
            return
        
        if self.contains(key):
            self.container[index].remove(key)

    def contains(self, key: int) -> bool:
        index = key % self.p
        if self.container[index] is None:
            return False

        return key in self.container[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
