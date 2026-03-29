class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = arr[:k]
        summ = sum(window)
        comb = []

        for R in range(k, len(arr)):
            print(window)
            if (summ / k) >= threshold:
                comb.append(window)
            window.append(arr[R])
            summ -= window.pop(0)
            summ += arr[R]
        if (summ / k) >= threshold:
            comb.append(window)
        return len(comb)
            
