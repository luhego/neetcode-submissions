class MyHashSet:

    def __init__(self):
        self.MOD = 997
        self.container = []
        for _ in range(self.MOD):
            self.container.append([])
        

    def add(self, key: int) -> None:
        index = key % self.MOD
        if key not in self.container[index]:
            self.container[index].append(key)
        

    def remove(self, key: int) -> None:
        index = key % self.MOD
        if key in self.container[index]:
            self.container[index].remove(key)
        
    def contains(self, key: int) -> bool:
        index = key % self.MOD
        return key in self.container[index]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)