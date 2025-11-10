from collections import deque nodes = ['A', 'B', 'C', 'D', 'E', 'F']
index = {n: i for i, n in enumerate(nodes)}

graph_matrix = [ [0, 1, 1, 0, 0, 0],
[1, 0, 0, 1, 1, 0],
[1, 0, 0, 0, 0, 1],
[0, 1, 0, 0, 1, 0],
[0, 1, 0, 1, 0, 1],
[0, 0, 1, 0, 1, 0]
]
visited_dfs = [False] * len(nodes) def dfs(node_index):
visited_dfs[node_index] = True print(nodes[node_index], end=" ")

for j in range(len(nodes)):
if graph_matrix[node_index][j] == 1 and not visited_dfs[j]:
dfs(j)

print("Depth First Search (DFS) starting from A:") dfs(index['A'])
print("\n")


graph_list = { 'A': ['B', 'C'],
'B': ['A', 'D', 'E'],
'C': ['A', 'F'],
'D': ['B', 'E'],
'E': ['B', 'D', 'F'],
'F': ['C', 'E']
}

def bfs(start): visited = set()
queue = deque([start]) visited.add(start)

print("Breadth First Search (BFS) starting from A:") while queue:
current = queue.popleft() print(current, end=" ")
for neighbor in graph_list[current]:

if neighbor not in visited: visited.add(neighbor) queue.append(neighbor)
print("\n")

bfs('A')

