class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]
        visit = set()
        def dfs(r, c):
            nonlocal orig
            ROWS, COLS = len(image), len(image[0])

            if min(r,c) < 0 or r == ROWS or c == COLS or image[r][c] != orig or (r, c) in visit:
                return

            if image[r][c] == orig:
                image[r][c] = color
            
            visit.add((r, c))
            
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            return
        dfs(sr,sc)
        return image