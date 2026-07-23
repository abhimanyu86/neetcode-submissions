class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0]*cols for _ in range(rows)]
        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    queue = deque()
                    queue.append((i, j))
                    visited[i][j] = 1
                    while queue:
                        x, y = queue.popleft()
                        for xx, yy in [(1,0),(0,1),(0,-1),(-1,0)]:
                            new_x, new_y = x+xx, y+yy
                            if new_x<0 or new_x>=rows or new_y<0 or new_y>=cols:
                                continue
                            if visited[new_x][new_y]==1:
                                continue
                            if grid[new_x][new_y]=="0":
                                continue
                            visited[new_x][new_y]=1
                            queue.append((new_x, new_y))
        return count