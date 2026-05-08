class HashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return sum(ord(char) for char in str(key)) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

ht = HashTable()
ht.put("Toyota", 4.5)
print(ht.get("Toyota"))
ht.put("Toyota", 7)
print(ht.get("Toyota"))