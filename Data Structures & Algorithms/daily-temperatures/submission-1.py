class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        stack = []
        i = -1
        j = 0
        k = 0

        while j < len(temperatures):  # Ensure the loop stops when j reaches the end of the list
            stack.append(temperatures[j])
            i += 1
            j += 1
            
            if stack[0] < stack[i]:  # This condition assumes that 'stack[i]' exists
                res.append(i)
                k += 1
                if k < len(temperatures):  # Check bounds before accessing temperatures[k]
                    temp = temperatures[k]
                    j = k + 1
                    i = 0
                    stack = [temp]
                else:
                    return res  # If k is out of bounds, return the result
            
            elif j == len(temperatures):  # Only executed at the end of the loop
                res.append(0)
                k += 1
                if k == len(temperatures):  # This is your existing check for termination
                    return res
                if k < len(temperatures):  # Additional safety check before accessing temperatures[k]
                    temp = temperatures[k]
                    j = k + 1
                    i = 0
                    stack = [temp]
        res.append(0)
        return res

            