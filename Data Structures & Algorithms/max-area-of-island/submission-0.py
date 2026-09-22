class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r,c))
            
            count = 1
            count += dfs(r+1,c)
            count += dfs(r-1,c)
            count += dfs(r,c+1)
            count += dfs(r,c-1)

            return count
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                res = max(res, dfs(i,j))

        return res
            
