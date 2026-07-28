from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = [[] for _ in range(n)]
        for u, v in edges:
            adjlist[u].append(v)
            adjlist[v].append(u)

        visited = [0 for _ in range(n)]
        count = 0

        for i in range(n):
            if visited[i] == 0:
                count += 1
                queue = deque()
                queue.append(i)
                visited[i] = 1

                while queue:
                    node = queue.popleft()
                    for adjnode in adjlist[node]:
                        if visited[adjnode] == 0:
                            visited[adjnode] = 1
                            queue.append(adjnode)

        return count