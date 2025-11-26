from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges) -> bool:
        if len(edges) != n-1: return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        q = deque([(0,-1)])
        visited = set()

        while q:
            node, parent = q.popleft()
            if node in visited :
                return False
            visited.add(node)
            for nei in adj[node]:
                if nei!=  parent:
                    q.append((nei, node))
        return len(visited) ==n