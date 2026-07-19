class MyHashMap:

    def __init__(self):
        self.MOD = 997
        self.container = []
        for _ in range(self.MOD):
            self.container.append([])

    def put(self, key: int, value: int) -> None:
        index = key % self.MOD
        found = False
        for i, entry in enumerate(self.container[index]):
            if entry[0] == key:
                self.container[index][i][1] = value
                found = True

        if not found:
            self.container[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.MOD
        for entry in self.container[index]:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.MOD

        to_remove = -1
        for i, entry in enumerate(self.container[index]):
            if entry[0] == key:
                to_remove = i
                break
        
        if to_remove != -1:
            self.container[index].pop(to_remove)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)