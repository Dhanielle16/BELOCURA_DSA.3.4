from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, start):

        visited = set()
        queue = deque([start])
        visited.add(start)
        result = []

        while queue:
            curr = queue.popleft()
            result.append(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):

        visited = set()
        result = []

        def dfs_helper(curr):
            visited.add(curr)
            result.append(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)
        return result

if __name__ == "__main__":
    print("=====================================================")
    print("  ASSESSMENT 3.3: GRAPH TRAVERSALS (BELOCURA)")
    print("=====================================================")


    graph = Graph()
    edges = [
        ('B', 'E1'), ('B', 'L'),
        ('E1', 'O'), ('E1', 'C'),
        ('L', 'U'), ('L', 'R'),
        ('O', 'A'), ('C', 'U')
    ]
    for u, v in edges:
        graph.add_edge(u, v)

    g_bfs = graph.bfs('B')
    g_dfs = graph.dfs('B')

    print(f"BFS result: {'-'.join(g_bfs)}")
    print(f"DFS result: {'-'.join(g_dfs)}")
    print("=====================================================")