class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        if grid[0][0] == 0:
            queue.append((0,0))
            visited.add((0,0))
        length = 1
        paths = [[1,0], [-1,0], [0, 1], [0,-1], [1,1], [1,-1], [-1,-1], [-1,1]]
        while len(queue) > 0:
            for i in range(len(queue)):
                curr = queue.popleft()
                visited.add(curr)
                if curr[0] == ROWS - 1 and curr[1] == COLS - 1:
                    return length
                
                for l, r in paths:
                    if min(curr[0] + l,curr[1] + r) < 0 or curr[0] + l == ROWS or curr[1] + r == COLS or grid[curr[0] + l][curr[1] + r] == 1 or (curr[0] + l,curr[1] + r) in visited:
                        continue
                    queue.append((curr[0] + l,curr[1] + r))
            length += 1

        return -1








        return -1