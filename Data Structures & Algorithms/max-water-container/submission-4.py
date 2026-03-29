class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        a = 0
        while l < r:
            # Calculate the area
            current_area = min(heights[l], heights[r]) * (r - l)
            # Update max area if current area is larger
            if a < current_area:
                a = current_area
                print("New max area:", a)
            # Move the pointer pointing to the shorter line
            if heights[l] < heights[r]:
                l += 1
                print('Move left pointer:', l)
            else:
                r -= 1
                print('Move right pointer:', r)
        return a