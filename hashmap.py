from dataclasses import dataclass

class MyHashMap:

    def __init__(self):
        self.entries = []

    def put(self, key: int, value: int) -> None:
        entry = Ent(key, value)
        try:
            idx = self.entries.index(entry)
            self.entries[idx] = entry
        except ValueError:
            self.entries.append(entry)


    def get(self, key: int) -> int:
        entry = Ent(key)
        try:
            idx = self.entries.index(entry)
            return self.entries[idx].key
        except ValueError:
            return -1

        

    def remove(self, key: int) -> None:
        entry = Ent(key)
        try:
            idx = self.entries.index(entry)
            self.entries.remove(entry)
        except ValueError:
            pass
    

@dataclass        
class Ent:
    key : int
    val : int = -1
    
    def __eq__(self, obj):
        if self.key == obj.key:
            return True
        else:
            return False

m = MyHashMap()
m.put(1, 1)
print(m.get(1))
m.put(1,2)
print(m.get(1))