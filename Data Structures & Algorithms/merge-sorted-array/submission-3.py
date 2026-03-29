class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m-1
        j = len(nums2)-1
        n = len(nums1)-1

        while j >= 0:
            print(nums1)
            if i < 0 or nums2[j] > nums1[i]:
                nums1[n] = nums2[j]
                j-=1
            else:
                nums1[n] = nums1[i]
                i -=1
            n -= 1

        