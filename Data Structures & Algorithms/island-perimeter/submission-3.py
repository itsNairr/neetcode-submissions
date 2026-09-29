class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        navigations = [[1,0], [-1,0], [0,1], [0,-1]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res += 4
                    for nav in navigations:
                        r = i + nav[0]
                        c = j + nav[1]
                        if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                            continue
                        res -= 1
                    
        return res
                         
