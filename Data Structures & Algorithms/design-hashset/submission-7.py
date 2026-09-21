class MyHashSet:

    def __init__(self):
        self.MOD = 1007
        self.buckets = [[] for _ in range(self.MOD)]
        

    def add(self, key: int) -> None:
        if not self.contains(key):
            bucket = key % self.MOD
            self.buckets[bucket].append(key)
        
    def remove(self, key: int) -> None:
        if self.contains(key):
            bucket = key % self.MOD
            self.buckets[bucket].remove(key)
        

    def contains(self, key: int) -> bool:
        bucket = key % self.MOD
        return key in self.buckets[bucket]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)