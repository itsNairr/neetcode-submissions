class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0
        def dfs(l,r):
            if min(l,r) < 0 or l == ROWS or r == COLS or (l,r) in visited or grid[l][r] == "0":
                return 0
            
            visited.add((l,r))

            dfs(l+1, r)
            dfs(l-1, r)
            dfs(l,r+1)
            dfs(l,r-1)

            return 1

        for i in range(ROWS):
            for j in range(COLS):       
                if dfs(i,j):
                    res += 1

        return res

