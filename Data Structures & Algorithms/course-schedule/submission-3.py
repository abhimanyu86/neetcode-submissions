class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        adj_list = [[] for _ in range(numCourses)]
        for u, v in prerequisites:      # to take u, need v first
            adj_list[v].append(u)       # edge goes v -> u
            indegree[u] += 1

        queue = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        res = []
        count = 0
        while queue:
            node = queue.pop()
            res.append(node)
            count += 1
            for adj_node in adj_list[node]:
                indegree[adj_node] -= 1
                if indegree[adj_node] == 0:
                    queue.append(adj_node)

        return True if count == numCourses else False