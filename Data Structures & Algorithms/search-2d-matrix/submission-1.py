class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, (ROWS*COLS)-1

        while L <= R:
            mid = L + (R - L) // 2
            
            val = matrix[mid // COLS][mid % COLS]

            if val == target:
                return True
            if val < target:
                L = mid + 1
            else:
                R = mid - 1
        
        return False
            

