from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v, weight=1):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

    def remove_edge(self, u, v):
        self.adj[u] = [(n, w) for n, w in self.adj[u] if n != v]
        if not self.directed:
            self.adj[v] = [(n, w) for n, w in self.adj[v] if n != u]

    def neighbors(self, v):
        return [n for n, w in self.adj.get(v, [])]

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        order = []
        visited.add(start)
        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        visited = set()
        order = []

        def _dfs(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.neighbors(node):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def has_path(self, start, end):
        return end in self.bfs(start)

    def __repr__(self):
        lines = []
        for v, edges in self.adj.items():
            neighbors = ", ".join(f"{n}(w={w})" for n, w in edges)
            lines.append(f"{v} -> [{neighbors}]")
        return "\n".join(lines)


g = Graph(directed=False)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

print("Graph Demo")
print(g)
print("BFS from A:", g.bfs("A"))
print("DFS from A:", g.dfs("A"))
print("Neighbors of D:", g.neighbors("D"))
print("Has path A -> E:", g.has_path("A", "E"))
print("Has path E -> A:", g.has_path("E", "A"))
g.remove_edge("D", "E")
print("After removing D-E, has path A -> E:", g.has_path("A", "E"))
