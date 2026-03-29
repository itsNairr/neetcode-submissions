class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        mcount = 0
        ccount = 0
        sign = None

        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                tsign = 1
            elif arr[i] < arr[i + 1]:
                tsign = -1
            else:
                tsign = 0

            print('before', sign, tsign, ccount, mcount)
            
            if sign is None or (sign == -1 and tsign == 1) or (sign == 1 and tsign == -1):
                pass
            else:
                ccount = 0
            sign = tsign
            print('after', sign, tsign, ccount, mcount)
            if tsign != 0:
                ccount += 1

            mcount = max(mcount, ccount)

        return mcount + 1