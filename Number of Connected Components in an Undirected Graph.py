from collections import deque, defaultdict

class Solution:
    def countComponents(self, n, edges):
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        components = 0

        for i in range(n):
            if i not in visited:
                components += 1
                q = deque([i])
                visited.add(i)

                while q:
                    node = q.popleft()
                    for nei in graph[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

        return components


def sdvefv(n, edges):
    adj = defaultdict(list)
    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)

    vi = set()
    con = 0
    for i in range(n):
        if i not in vi:
            vi.add(i)
            con+=1
            q=deque([i])
            while q:
                l = q.popleft()
                for nei in adj[l]:
                    if nei not in vi:
                        vi.add(nei)
                        q.append(nei)
    return con
