class Node(object):
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def getKey(self):
        return self.key

    def getValue(self):
        return self.value

class MapIterator():
    def __init__(self,mas):
        self.mas = mas
        self.current = 0
        self.size = len(mas)

    def __next__(self):
        if self.current < self.size:
            item = self.mas[self.current]
            self.current += 1
            if item is None:
                return self.__next__()
            else:
                return item.getValue()
        else:
            raise StopIteration



class Map(object):
    def __init__(self,size):
        self.mas = [None]*size
        self.size = size
        self.count = 0

    def put(self, key, value):
        if self.count / self.size > 0.7:
            self.resize()
        hashcode = hash(key)
        hashKey = hashcode % self.size
        while self.mas[hashKey] is not None:
            hashKey = (hashKey + 1) % self.size
        self.mas[hashKey] = Node(key,value)
        self.count += 1

    def delete(self, key):
        hashcode = hash(key)
        hashKey = hashcode % self.size
        while self.mas[hashKey] is not None:
            if self.mas[hashKey].getKey() is key:
                break
            hashKey = (hashKey + 1) % self.size
        self.mas[hashKey] = None
        self.count -= 1

    def get(self,key):
        hashcode = hash(key)
        hashKey = hashcode % self.size
        while self.mas[hashKey] is not None:
            if self.mas[hashKey].getKey() is key:
                break
            hashKey = (hashKey + 1) % self.size
        if self.mas[hashKey] is None:
            return None
        else:
            return self.mas[hashKey].getValue()

    def __iter__(self):
        return MapIterator(self.mas)

    def resize(self):
        newSize = self.size*2
        newMas = [None]*newSize
        for node in self.mas:
            if node is not None:
                hashkey = node.getKey() % newSize
                newMas[hashkey] = node
        self.mas = newMas
        self.size = newSize




map = Map(1)

map.put(3,"string 3")
map.put(6,"string 6")
map.put(7,"string 7")
map.put(10,"string 10")


print(map.get(3))
print(map.get(6))
map.delete(7)
print(map.get(7))
print(map.get(10))

for item in map:
    print(item)