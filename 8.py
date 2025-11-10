class Node:
def 	init	(self, key): self.key = key self.left = None self.right = None

class BST:
def 	init	(self): self.root = None

def insert(self, key):
self.root = self._insert(self.root, key)

def _insert(self, root, key): if root is None:
return Node(key) if key < root.key:
root.left = self._insert(root.left, key) elif key > root.key:

root.right = self._insert(root.right, key) return root

def search(self, key):
return self._search(self.root, key)

def _search(self, root, key):
if root is None or root.key == key: return root
if key < root.key:
return self._search(root.left, key) else:
return self._search(root.right, key)

def _min_value_node(self, node): current = node
while current.left is not None: current = current.left
return current

def delete(self, key):
self.root = self._delete(self.root, key)

def _delete(self, root, key): if root is None:
return root
if key < root.key:
root.left = self._delete(root.left, key) elif key > root.key:

root.right = self._delete(root.right, key) else:
if root.left is None: temp = root.right root = None return temp
elif root.right is None: temp = root.left root = None
return temp
temp = self._min_value_node(root.right) root.key = temp.key
root.right = self._delete(root.right, temp.key) return root

def inorder(self): res = []
self._inorder(self.root, res) return res

def _inorder(self, root, res): if root:
self._inorder(root.left, res) res.append(root.key) self._inorder(root.right, res)

# Running the code
if 		name	== "	main	": bst = BST()

# Insert keys bst.insert(50) bst.insert(30) bst.insert(20) bst.insert(40) bst.insert(70) bst.insert(60) bst.insert(80)
print("Inorder traversal of the BST:", bst.inorder())

key = 40
found = bst.search(key) if found:
print(f"Key {key} found in BST.") else:
print(f"Key {key} not found in BST.")

bst.delete(20)
print("Inorder traversal after deleting 20:", bst.inorder())

bst.delete(30)
print("Inorder traversal after deleting 30:", bst.inorder())

bst.delete(50)
print("Inorder traversal after deleting 50:", bst.inorder())
