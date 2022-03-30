import json

class HashTable:
    def __init__(self) -> None:
        self.count = 0
        self.store = {}

    def add_val(self, values):
        # common interview question to find duplicates in a list
        duplicates = set()
        for val in values:
            if self.contains(val):
                duplicates.add(val)
            try:
                val_hash = hash(val)
            except Exception as exc:
                return f"Error occured {str(exc)}"
            self.count = self.count + 1
            self.store[val_hash] = val
        if duplicates:
            return f"Duplicate values: {duplicates}"


    def contains(self, val):
        try:
            val_hash = hash(val)
        except Exception as exc:
            return f"Error occured {str(exc)}"
        keys = self.store.keys()
        return True if val_hash in keys else False

    def remove_val(self, val):
        hash_val = hash(val)
        keys = self.store.keys()
        if hash_val in keys:
            del self.store[hash_val]
        else:
            return "Item doesnot exist in hashtable"
        return "Deleted"

    def __repr__(self) -> str:
        return " , ".join(str(item) for key, item in self.store.items())

hash_table = HashTable()
p = [1,2,3,3,4,5,1,4,4]
q = [1,2,3,4,5,6,7]
hash_table1 = HashTable()

print(hash_table.add_val(p))
print(hash_table1.add_val(q))
print(hash_table1.remove_val('pea'))
print(hash_table1)

print(hash_table1.remove_val(4))

print(hash_table)
print(hash_table1)

