class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        summ = sum(arr[L:k])
        comb = 0

        for R in range(k, len(arr)):
            if (summ / k) >= threshold:
                comb += 1
            summ = summ - arr[L] + arr[R]
            L += 1
        if (summ / k) >= threshold:
            comb += 1
        return comb
            
