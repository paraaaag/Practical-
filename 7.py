class HashTable:
def 	init	(self, size): self.size = size
self.table = [None] * size

def hash_function(self, key): return key % self.size

def insert(self, key):
index = self.hash_function(key) start_index = index

while self.table[index] is not None and self.table[index] != "DELETED":
if self.table[index] == key: print(f"Key {key} already exists!") return
index = (index + 1) % self.size if index == start_index:


keys.")
print("Hash Table is full! Cannot insert more return

self.table[index] = key
print(f"Key {key} inserted at index {index}")

def search(self, key):
index = self.hash_function(key) start_index = index

while self.table[index] is not None: if self.table[index] == key:
print(f"Key {key} found at index {index}") return index
index = (index + 1) % self.size if index == start_index:
break

print(f"Key {key} not found.") return None

def delete(self, key):
index = self.hash_function(key) start_index = index

while self.table[index] is not None: if self.table[index] == key:
self.table[index] = "DELETED"

print(f"Key {key} deleted from index {index}") return
index = (index + 1) % self.size if index == start_index:
break
print(f"Key {key} not found. Cannot delete.") def display(self):
print("\nHash Table Contents:") for i in range(self.size):
print(f"Index {i}: {self.table[i]}") print()


if 	name	== "	main	":
size = int(input("Enter size of hash table: ")) ht = HashTable(size)

while True: print("\nOperations:") print("1. Insert a key") print("2. Search for a key") print("3. Delete a key") print("4. Display table") print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
key = int(input("Enter key to insert: ")) ht.insert(key)

elif choice == 2:
key = int(input("Enter key to search: ")) ht.search(key)

elif choice == 3:
key = int(input("Enter key to delete: ")) ht.delete(key)

elif choice == 4: ht.display()

elif choice == 5: print("Exiting...") break

else:
print("Invalid choice. Try again.")
