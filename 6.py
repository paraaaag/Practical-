using Division Method and Chaining
class HashTable:
def 	init	(self, size=10): self.size = size
self.table = [[] for _ in range(size)] # each index holds a list (for chaining)

# Hash function (Division method) def hash_function(self, key):
return key % self.size

# Insert key-value pair
def insert(self, key, value):
index = self.hash_function(key)
# Check if key already exists; if yes, update for pair in self.table[index]:
if pair[0] == key: pair[1] = value
print(f"Updated key {key} with new value '{value}' at index {index}")
return
# Otherwise, append a new pair

self.table[index].append([key, value])
print(f"Inserted key {key} with value '{value}' at index
{index}")

# Search for a key def search(self, key):
index = self.hash_function(key) for pair in self.table[index]:
if pair[0] == key:
print(f"Key {key} found at index {index} with value '{pair[1]}'")
return pair[1] print(f"Key {key} not found!") return None

# Delete a key-value pair def delete(self, key):
index = self.hash_function(key) for pair in self.table[index]:
if pair[0] == key: self.table[index].remove(pair)
print(f"Key {key} deleted from index {index}") return
print(f"Key {key} not found for deletion!")

# Display hash table def display(self):
print("\nHash Table State:")
for i, bucket in enumerate(self.table): print(f"Index {i}: {bucket}")


# --- Example Usage ---

if 		name	== "	main	": ht = HashTable()

# Insert values ht.insert(15, "Apple") ht.insert(25, "Banana") ht.insert(35, "Cherry") ht.insert(5, "Mango")
ht.display() # Search
ht.search(25)
ht.search(100)

# Delete ht.delete(15) ht.delete(99)

ht.display()
