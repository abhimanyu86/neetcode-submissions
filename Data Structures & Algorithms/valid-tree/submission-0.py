from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjlist = [[] for _ in range(n)]
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        visited = [0 for _ in range(n)]
        queue = deque()
        queue.append(0)
        visited[0] = 1

        while queue:
            node = queue.popleft()
            for adjnode in adjlist[node]:
                if visited[adjnode] == 0:
                    visited[adjnode] = 1
                    queue.append(adjnode)

        return all(v == 1 for v in visited)